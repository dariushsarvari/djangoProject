from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView


# Create your views here.

def products_view(request):
    products = Product.objects.all()
    context = {
        'products_list': products
    }
    return render(request, 'products_list.html', context)


class ProductsView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products_list.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        return Product.objects.all()


def product_detail(request, productID):
    # product = Product.objects.get(id=productID)
    # product = get_object_or_404(Product, id=productID)

    # qs = Product.objects.filter(id=productID)
    # if qs.exists() and qs.count() == 1:
    #     product = qs.first()
    # else:
    #     raise Http404("Product Not Found")

    product = Product.objects.get_product_by_id(productID)
    if product is None:
        raise Http404("Product not found!!!!!!!!!!!")

    context = {
        "product": product
    }
    return render(request, 'product_detail.html', context)


class ProductDetail(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        productID = self.kwargs.get('pk')
        product = Product.objects.get_product_by_id(productID)
        if product is None:
            raise Http404("Product not found$$$$$$$$")
        return product


class ProductActiveList(ListView):
    template_name = 'products_list.html'

    def get_queryset(self):
        return Product.objects.get_active_show_products()


class ProductActiveDetail(DetailView):
    template_name = 'product_detail.html'

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductShowWithSlug(DetailView):
    template_name = 'product_detail.html'

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            product = Product.objects.get(slug=slug, actived=True)
        except Product.DoesNotExist:
            raise Http404("Product does not found")
        except Product.MultipleObjectsReturned:
            raise Http404("Multiple Objects Returned")

        return product

