from django.shortcuts import render
from contents.views import About


def header(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Header.html', context)

def Search(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Search.html', context)


def Capsule(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Capsule.html', context)

def Bottom(request, *args, **kwargs):
    about = About.objects.filter(active=True).last()


    context = {
    'about': about,

    }
    return render(request, 'shared/Bottom.html', context)

def Sidebar(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/Sidebar.html', context)

def welcome(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/welcome.html', context)

def ShareActionSheet(request, *args, **kwargs):
    context = {
    }
    return render(request, 'shared/ShareActionSheet.html', context)








