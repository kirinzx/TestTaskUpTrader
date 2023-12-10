from django.urls import path
from .views import get_menu, get_menus

urlpatterns = [
    path('menu/<str:menu_name>/item/<int:item_pk>', get_menu),
    path('menu',get_menus)
]
