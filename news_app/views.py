from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from unicodedata import category
from django.db.models import Q
from .forms import CommentForm
from .models import News, Photos, Category, Comment
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin


def news_list_view(request):
    newslar=News.objects.all()
    lastest_news = News.objects.all().order_by('-created_time')[:5]
    all_news = News.objects.all().order_by('-created_time')
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
        'all_news':all_news,
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



def news_detail_view(request, news):
    new = get_object_or_404(News, slug=news, status=News.Status.Published)

    context = {}

    hit_count = get_hitcount_model().objects.get_for_object(new)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_counted'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = new
            comment.user = request.user
            comment.save()
            return redirect('news_detail', news=new.slug)

    else:
        form = CommentForm()

    comments = new.comments.filter(active=True)
    new_comment = None
    comment_count = len(comments)

    three_news = News.objects.filter(
        category__name=new.category.name,
        status=News.Status.Published
    ).exclude(id=new.id)[:3]

    category_list = Category.objects.all()

    context = {
        'news': new,
        'category_list': category_list,
        'three_news': three_news,
        'form': form,
        'comments': comments
    }
    return render(request, 'single_page.html', context)



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


class NewsDeleteview(DeleteView):
    model = News
    success_url = reverse_lazy('news_list')
    template_name = 'crud/delete.html'

class NewsCreateview(CreateView):
    model = News
    fields = ['title', 'slug', 'body', 'category', 'image', 'status']
    template_name = 'crud/create.html'
    success_url = reverse_lazy('news_list')

class SearchResultsList(ListView):
    model = News
    template_name = 'search_results.html'
    context_object_name = 'barcha_yangiliklar'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

