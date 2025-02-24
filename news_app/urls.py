from django.urls import path
from . import views
from .views import news_list_view, news_detail_view, contact_view, local_news_view, category_news_list_view, \
    NewsUpdateview, NewsDeleteview, NewsCreateview,SearchResultsList

urlpatterns = [
    path('', news_list_view, name='news_list'),
    path('news/<slug:news>', news_detail_view, name='news_detail'),

    path('news/category/<int:category_id>/', category_news_list_view, name='category_link'),
    path('contact/',contact_view, name='contact'),
    path('news/<slug>/update/', NewsUpdateview.as_view(), name='update'),
    path('news/<slug>/delete/', NewsDeleteview.as_view(), name='delete'),
    path('news/create/', NewsCreateview.as_view(), name='create'),
    path('local/',local_news_view, name='local_news'),
    path('searchresult/', SearchResultsList.as_view(), name='search_results'),
]


