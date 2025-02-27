from django.core.exceptions import PermissionDenied
from django.db.models import Q
from oscar.apps.dashboard.catalogue import views as originalviews
from shop.apps.catalogue_dashboard.dashboard.catalogue.forms import ProductForm, ProductSearchForm
from shop.apps.catalogue_dashboard.dashboard.catalogue.tables import ProductTable
from rules.contrib.views import PermissionRequiredMixin
from icecream import ic

class ProductListView(originalviews.ProductListView):
    table_class = ProductTable
    form_class = ProductSearchForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['seller'] = 'Main Seller'
        ic("Inside get_context_data")
        ic(ctx)
        ic(ctx['products'])
        return ctx


    def apply_search(self, queryset):
        qs = super().apply_search(queryset)
        data = self.form.cleaned_data
        seller = data['seller']

        if seller:
            qs = qs.filter(seller=seller)

        return qs

class ProductCreateRedirectView(originalviews.ProductCreateRedirectView):
    pass

class ProductCreateUpdateView(originalviews.ProductCreateUpdateView, PermissionRequiredMixin):
    form_class = ProductForm
    permission_required = 'products.can_edit_product'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.has_perm('products.can_edit_product', obj):
            raise PermissionDenied
        return obj

    # def get_permission_object(self):
    #     return self.get_object()

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user =  self.request.user
        
        if user.is_superuser:
            pass
        elif user.seller_admins.exists():
            form.fields['seller'].queryset = user.seller_admins.all()
        elif hasattr(user, 'seller'):
            form.fields.pop('seller', None)
        
        return form

    def form_valid(self, form):
        user = self.request.user

        if hasattr(user, 'seller'):
            form.instance.seller = user.seller

        return super().form_valid(form)

class ProductDeleteView(originalviews.ProductDeleteView):
    pass

class StockAlertListView(originalviews.StockAlertListView):
    pass


class CategoryListView(originalviews.CategoryListView):
    pass


class CategoryDetailListView(originalviews.CategoryDetailListView):
    pass


class CategoryListMixin(originalviews.CategoryListMixin):
    pass


class CategoryCreateView(originalviews.CategoryCreateView):
    pass


class CategoryUpdateView(originalviews.CategoryUpdateView):
    pass


class CategoryDeleteView(originalviews.CategoryDeleteView):
    pass


class ProductLookupView(originalviews.ProductLookupView):
    pass


class ProductClassCreateUpdateView(originalviews.ProductClassCreateUpdateView):
    pass

class ProductClassCreateView(originalviews.ProductClassCreateView):
    pass
    # form_class = ProductClassForm

    # def __init__(self, *args, **kwargs):
    #     ic("Inside __init__")
    #     ic(*args)
    #     ic(**kwargs)
    #     super().__init__(*args, **kwargs)

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     user = self.request.user
    #     if user.is_superuser:
    #         pass
    #     elif hasattr(user, 'seller_admins') and user.seller_admins.exists():
    #         form.fields['seller'].queryset = user.seller_admins.all()
    #     elif hasattr(user, 'seller'):
    #         form.fields.pop('seller', None)

    #     return form

    # def form_valid(self, form):
    #     user = self.request.user

    #     if hasattr(user, 'seller'):
    #         form.instance.seller = user.seller

    #     return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     ic("inside get")
    #     ic(*args)
    #     ic(**kwargs)
    #     return super().get(request, *args, **kwargs)

    # def get_context_data(self, *args, **kwargs):
    #     ctx = super().get_context_data(*args, **kwargs)
    #     ic("inside get_context_data")
    #     ic(self.form_class.__module__)
    #     ic(ctx)
    #     return ctx



class ProductClassUpdateView(originalviews.ProductClassUpdateView):
    pass


class ProductClassListView(originalviews.ProductClassListView):
    pass
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     ic(self.request.user)
    #     # if user is superuser then don't filter any of the Product Classes
    #     if self.request.user.is_superuser or self.request.user.groups.filter(name='Seller Admin').exists():
    #         return qs
    #     if hasattr(self.request.user, 'seller'):
    #         qs.filter(Q(seller__id=1) | Q(seller__id=self.request.user.seller.id))
    #         return qs
    #     if self.request.user.seller_admins.count() > 0:
    #         qs.filter(Q(seller__id=1) | Q(seller__admin=self.request.user))
    #         return qs
    #     return qs.none()


class ProductClassDeleteView(originalviews.ProductClassDeleteView):
    pass


class AttributeOptionGroupCreateUpdateView(originalviews.AttributeOptionGroupCreateUpdateView):
    pass


class AttributeOptionGroupCreateView(originalviews.AttributeOptionGroupCreateView):
    pass


class AttributeOptionGroupUpdateView(originalviews.AttributeOptionGroupUpdateView):
    pass


class AttributeOptionGroupListView(originalviews.AttributeOptionGroupListView):
    pass


class AttributeOptionGroupDeleteView(originalviews.AttributeOptionGroupDeleteView):
    pass


class OptionListView(originalviews.OptionListView):
    pass

class OptionCreateUpdateView(originalviews.OptionCreateUpdateView):
    pass


class OptionCreateView(originalviews.OptionCreateView):
    pass


class OptionUpdateView(originalviews.OptionUpdateView):
    pass


class OptionDeleteView(originalviews.OptionDeleteView):
    pass

