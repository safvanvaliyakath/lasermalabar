# Generated by Django 3.2.9 on 2021-11-25 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('malabarapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='images')),
                ('dfile', models.FileField(upload_to='files')),
                ('categ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='malabarapp.category')),
            ],
        ),
    ]
