from django.shortcuts import render
# from matplotlib import context
from .models import Product_type
from django.core.paginator import Paginator


def product(request):
    
    product_types = Product_type.objects.all()
    paginator = Paginator(product_types, 3)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    
    prev = '?page={}'.format(page.previous_page_number()) if page.has_previous() else ''
    next = '?page={}'.format(page.next_page_number()) if page.has_next() else ''

    context = {
        'product_types': page,
        'is_paginated': is_paginated,
        'prev_url': prev,
        'next_url': next,
    }

    return render(request, 'product/index.html', context=context)
