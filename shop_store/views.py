from django.shortcuts import render



def index(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact.html')


def about_us(request):
    return render(request, 'about.html')