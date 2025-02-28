from django.shortcuts import render

def home(request):
    """نمایش صفحه اصلی سایت"""
    return render(request, 'home.html')

