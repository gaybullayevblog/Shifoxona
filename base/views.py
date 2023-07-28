from django.shortcuts import render

# Create your views here.


def home(req):
    return render(req, "pages/home.html")


def about(req):
    return render(req, "pages/about.html")


def workers(req):
    return render(req, "pages/workers.html")


def departments(req):
    return render(req, "pages/departments.html")


def blog(req):
    return render(req, "pages/blog.html")


def contact(req):
    return render(req, "pages/contact.html")

def download(req):
    return render(req, "pages/download.html")
