from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from webapp.forms import ProductForm
from webapp.models import Product


class ProductListView(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_context_data(self,*, object_list=None, **kwargs):
        return super().get_context_data(object_list=object_list,**kwargs)

    def get_queryset(self):
        data = Product.objects.all()
        return data


class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product
    paginate_reviews_by = 5
    paginate_reviews_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews, page, is_paginated = self.paginate_reviews(self.object)
        context['reviews'] = reviews
        context['page_obj'] = page
        context['is_paginated'] = is_paginated

        return context

    def paginate_reviews(self, product):
        reviews = product.review.all().order_by('-created_at')
        if reviews.count() > 0:
            paginator = Paginator(reviews, self.paginate_reviews_by, orphans=self.paginate_reviews_orphans)
            page_number = self.request.GET.get('page', 1)
            page = paginator.get_page(page_number)
            is_paginated = paginator.num_pages > 1
            return page.object_list, page, is_paginated
        else:
            return reviews, None, False


class ProductCreateView(CreateView):
    template_name = 'product/product_create.html'
    form_class = ProductForm
    model = Product
    permission_required = 'webapp.add_project'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ProductUpdateView(UpdateView):
    template_name = 'product/product_update.html'
    form_class = ProductForm
    model = Product
    permission_required = 'webapp.change_project'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_product'

    # def has_permission(self):
    #     return super().has_permission() and self.request.user in self.object.project.user.all()


