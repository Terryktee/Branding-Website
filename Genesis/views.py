from django.shortcuts import render
from .models import Product,Product_Image
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.http import JsonResponse , Http404

#Class Index View

class ProductIndexView(ListView):

    model = Product
    template_name = 'Genesis/home.html'
    context_object_name = 'products'
    paginate_by = 8

#view specific product 
class ProductDetailView(DetailView):
    model = Product
    template_name = "Genesis/product_view.html" 
   
    