from threading import activeCount

from django.contrib import admin
from .models import Category, News, Photos, Comment
from django.contrib.admin import ModelAdmin

admin.site.register(Photos)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','news', 'body','created')
    list_filter = ('user','news')
    actions = ['enable_comments','disable_comments']

    def enable_comments(self,request,queryset):
        queryset.update(active = True)


    def disable_comments(self,request,queryset):
        queryset.update(active=False)

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
admin.site.register(Comment, CommentAdmin)
