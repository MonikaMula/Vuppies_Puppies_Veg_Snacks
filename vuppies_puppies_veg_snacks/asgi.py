"""
ASGI config for vuppies_puppies_veg_snacks project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vuppies_puppies_veg_snacks.settings')

application = get_asgi_application()
