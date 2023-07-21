from django.contrib import admin
from .models import Author, Category, Post,  Comment
from django import forms









# Действие в админ панели 'Снять пост с публикации'
def public_off(modeladmin, request, queryset):
    queryset.update(public=False)


public_off.short_description = 'Снять пост с публикации'


# Действие в админ панели 'Опубликовать пост'
def public_on(modeladmin, request, queryset):
    queryset.update(public=True)


public_on.short_description = 'Опубликовать пост'








admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)

