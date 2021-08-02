from django.shortcuts import render

# Create your views here.


def homerender(request):
    return render(request, 'friend/home-page.html')
