from django.urls import path
from . import views
urlpatterns = [
    path('blog.html',views.blog,name='blog'),
    #if need a client page uncomment
    #path('client.html',views.client,name='client'),
    path('about.html',views.about,name='about'),
    path('contact.html',views.contact,name='contact'),
    path('packages.html',views.packages,name='packages'),
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
]