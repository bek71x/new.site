from django.urls import path
from .views import news_list_view, news_detail_view, contact_view, local_news_view, category_news_list_view

urlpatterns = [
    path('', news_list_view, name='news_list'),  # Добавлена запятая
    path('news/<slug:news>', news_detail_view, name='news_detail'),  # Убедитесь, что слеш "/" в конце указан
    path('news/category/<int:category_id>/', category_news_list_view, name='category_link'),  # Убедитесь, что слеш "/" в конце указан
    path('contact/',contact_view, name='contact'),
    path('local/',local_news_view, name='local_news')
]
