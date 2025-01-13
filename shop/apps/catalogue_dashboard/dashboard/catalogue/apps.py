import oscar.apps.dashboard.catalogue.apps as apps
from icecream import ic

class CatalogueDashboardConfig(apps.CatalogueDashboardConfig):
    name = 'shop.apps.catalogue_dashboard.dashboard.catalogue'

    def ready(self):
        from .views import ( 
            ProductListView, ProductClassCreateUpdateView, ProductClassCreateView, ProductClassDeleteView,
            ProductClassListView, ProductClassUpdateView, ProductCreateRedirectView, ProductCreateUpdateView,
            ProductDeleteView, ProductLookupView, AttributeOptionGroupCreateUpdateView, AttributeOptionGroupCreateView,
            AttributeOptionGroupDeleteView, AttributeOptionGroupListView, AttributeOptionGroupUpdateView,
            CategoryListView, CategoryCreateView, CategoryDeleteView, CategoryDetailListView, CategoryUpdateView,
            StockAlertListView, OptionCreateView, OptionDeleteView, OptionListView,
            OptionUpdateView
        )

        ret = super().ready()
        self.product_list_view = ProductListView
        self.product_lookup_view = ProductLookupView
        self.product_create_redirect_view = ProductCreateRedirectView
        self.product_createupdate_view = ProductCreateUpdateView
        self.product_delete_view = ProductDeleteView

        self.product_class_create_view = ProductClassCreateView
        self.product_class_update_view = ProductClassUpdateView
        self.product_class_list_view = ProductClassListView
        self.product_class_delete_view = ProductClassDeleteView

        self.category_list_view = CategoryListView
        self.category_detail_list_view = CategoryDetailListView
        self.category_create_view = CategoryCreateView
        self.category_update_view = CategoryUpdateView
        self.category_delete_view = CategoryDeleteView

        self.stock_alert_view = StockAlertListView

        self.attribute_option_group_create_view = AttributeOptionGroupCreateView
        self.attribute_option_group_list_view = AttributeOptionGroupListView
        self.attribute_option_group_update_view = AttributeOptionGroupUpdateView
        self.attribute_option_group_delete_view = AttributeOptionGroupDeleteView

        self.option_list_view = OptionListView
        self.option_create_view = OptionCreateView
        self.option_update_view = OptionUpdateView
        self.option_delete_view = OptionDeleteView

        return ret
