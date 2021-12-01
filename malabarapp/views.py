from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from . models import *
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.db.models import Q
# Create your views here.

def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug != None:
        c_page = get_object_or_404(category,slug=c_slug)
        prodt=products.objects.filter(categ=c_page)
    else:
        prodt=products.objects.all()
    cat=category.objects.all()
    paginator=Paginator(prodt,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,'home.html',{'products':prodt,'categories':cat,'pg':pro})

def add(request):
    categ=category.objects.all()
    if request.method == 'POST':
        title=request.POST['name']
        cate=category.objects.get(name=request.POST['category'])
        desc=request.POST['description']
        image=request.FILES.get('img1',False)
        if image == False:
            image = "11.jpg"
        file=request.FILES.get('dxf',False)
        if file == False:
            file="11.jpg"
        s=products(title=title,categ=cate,desc=desc,img=image,dfile=file)
        s.save()
        return redirect('/')
    return render(request,'add.html',{'categories':categ})

class detailview(DetailView):
    model = products
    template_name = 'detail.html'
    context_object_name = 'obj1'

def search(request):
    product=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        product=products.objects.all().filter(Q(title__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':product})

# class Deleteview(DeleteView):
#     model = products
#     template_name = 'delete.html'
#     success_url = reverse_lazy('delete')

def Deleteview(request,id):
    if request.method == 'POST':
        obj2=products.objects.get(id=id)
        obj2.delete()
        return redirect('/')
    return render(request,'delete.html')
