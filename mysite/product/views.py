from django.shortcuts import render

from .models import Product_type
from django import forms

from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView

from django.contrib import messages
from django.urls import reverse_lazy 


def product(request):
    
    product_types = Product_type.objects.order_by('-id')
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


class Product_typeForm(forms.ModelForm):
    class Meta:
        model = Product_type
        fields = ['title']
        lables = {
            'title': 'Название типа продукта',
        }
        widgets = {
            'title': forms.TimeInput(attrs = {'class': 'form-control'}),
        }


class Product_typeCreate(CreateView):
    model = Product_type
    form_class = Product_typeForm
    template_name = 'product/create_product_type.html'
    success_url = '/product/'


class Product_typeUpdate(UpdateView):
    model = Product_type
    form_class = Product_typeForm
    template_name = 'product/update_product_type.html'
    success_url = '/product/'


class Product_typeDelete(DeleteView):
    model = Product_type
    context_object_name = 'product'
    success_url = reverse_lazy('product_url')

    def form_valid(self, form):
        messages.success(self.request, "The task was deleted siccessfully")
        return super(Product_typeDelete, self).form_valid(form)
    