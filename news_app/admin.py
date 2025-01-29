from django.contrib import admin
from .models import Category, News, Photos
from django.contrib.admin import ModelAdmin

admin.site.register(Photos)

class NewsAdmin(ModelAdmin):
    list_display = ['title', 'category', 'status', 'publish_time']
    list_filter = ['status', 'category']
    date_hierarchy = 'created_time'
    prepopulated_fields = {'slug': ['title']}
    search_fields = ('title', 'body')

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(News, NewsAdmin)
