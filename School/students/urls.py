from django.urls import path

from students import views

urlpatterns = [
    path('',views.about,name="about"),
    path('contact',views.contact, name="contact"),
    path('classes',views.classes, name="classes")

]
