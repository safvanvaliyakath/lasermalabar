from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>',views.home,name='product_categ'),
    path('search/',views.search,name='search'),
    path('add/',views.add,name='add'),
    path('detail/<int:pk>', views.detailview.as_view(), name='detailview'),
    path('delete/<int:id>',views.Deleteview,name='delete'),
]