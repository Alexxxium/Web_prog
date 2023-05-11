from django.shortcuts import render


def product(request):
    return render(request, 'product/index.html')
