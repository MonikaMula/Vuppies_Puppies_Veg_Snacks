from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    label = 'unique_products' # Make sure this label is unique if there are multiple product-related apps
