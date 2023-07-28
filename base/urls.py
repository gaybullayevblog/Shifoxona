from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("workers/", views.workers, name="workers"),
    path("departments/", views.departments, name="departments"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("download/", views.download, name="download"),
]