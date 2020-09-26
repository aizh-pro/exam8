from django.views.generic import ListView

from webapp.models import Product


class ProductListView(ListView):
    template_name = 'product/index.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_context_data(self,*, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list,**kwargs)

    def get_queryset(self):
        data = Product.objects.all()
        return data
