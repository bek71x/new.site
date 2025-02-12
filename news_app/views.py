from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from unicodedata import category

from .models import News, Photos, Category


def news_list_view(request):
    newslar=News.objects.all()
    lastest_news = News.objects.all().order_by('-created_time')[:5]
    local_news = News.objects.filter(category__name ='Mahalliy').order_by('-created_time')[:5]
    techno_news = News.objects.filter(category__name ='Texnologiya').order_by('-created_time')[:5]
    iqsodiy_news = News.objects.filter(category__name ='Iqsodiyot').order_by('-created_time')[:5]
    sport_news = News.objects.filter(category__name ='Sport').order_by('-created_time')[:5]
    xorij_news = News.objects.filter(category__name ='Xorij').order_by('-created_time')[:5]
    avto_news = News.objects.filter(category__name ='Avto').order_by('-created_time')[:5]
    photos = Photos.objects.all()[:6]
    category_list = Category.objects.all()

    context ={
        'news_list': newslar,
        'lastest_news': lastest_news,
        'local_news': local_news,
        'techno_news': techno_news,
        'iqsodiy_news': iqsodiy_news,
        'sport_news': sport_news,
        'xorij_news': xorij_news,
        'avto_news': avto_news,
        'photos': photos,
        'category_list': category_list,
    }

    return render(request,'index.html',context)


def news_detail_view(request,news):
    new = News.objects.get(slug = news)
    category_list = Category.objects.all()
    context = {
        'news':new,
        'category_list':category_list,
    }
    return render(request,'single_page.html',context)


def contact_view(request):
    return render(request,'contact.html')

def local_news_view(request):
    news_list = News.published.filter()



def category_news_list_view(request, category_id):
    category = Category.objects.get(id = category_id)
    newws_list = News.objects.filter(category__name =category.name)
    category_list = Category.objects.all()
    context = {
        'newws_list' : newws_list,
        'category' : category,
        'category_list' : category_list,
    }
    return render(request, 'category_news.html', context)

def category_list(request):
    category_list = Category.objects.all()

    return render(request, 'base.html', {'category_list': category_list})

class NewsUpdateview(UpdateView):
    model = News
    template_name = 'crud/update.html'
    fields = ['title','slug','body','category','image','status']
    # form_class = NewsUpdateForm()

class NewsDeleteview(DeleteView):
    model = News
    success_url = reverse_lazy('news_list')
    template_name = 'crud/delete.html'

class NewsCreateview(CreateView):
    model = News
    fields = ['title', 'slug', 'body', 'category', 'image', 'status']
    template_name = 'crud/create.html'
    success_url = reverse_lazy('news_list')