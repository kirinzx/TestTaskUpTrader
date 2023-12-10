from django.contrib import admin
from .models import MenuItem, Menu

admin.site.register([MenuItem, Menu])
