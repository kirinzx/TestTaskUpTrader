from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.title}. id: {self.pk}'


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE,related_name='parents')
    url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name}. id: {self.pk}. menu: {self.menu.title}'