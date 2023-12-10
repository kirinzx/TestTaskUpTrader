from django.shortcuts import render
from django.http import HttpRequest

def get_menu(request: HttpRequest, menu_name: str=None, item_pk: int=None):
    return render(request, 'menu.html', context={
        'menu_name': menu_name,
        'item_pk': item_pk
    })

def get_menus(request: HttpRequest):
    return render(request,'menu.html',context={
        'menu_names': request.GET.getlist('menu_name')
    })