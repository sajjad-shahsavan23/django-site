from django.db.models.base import Model as Model
from django.contrib.auth.models import User
from django.views.generic import ListView ,DetailView
from django.shortcuts import render,get_object_or_404
from .models import Art ,Category


# Create your views here.

#def home(request , page=1):
#    art_list = Art.objects.published()
#    paginator = Paginator(art_list, 5) 
#    articles = paginator.get_page(page)
#    context = {
#        "articles": articles,
#    }
#    return render(request,"blog/home.html",context)

class ArticleList(ListView):
    #model = Art
    #template_name = 'blog/home.html'
    #context_object_name = 'articles'
    queryset = Art.objects.published()
    paginate_by = 5


#def detail(request,slug):
#    context = {
#        "article": get_object_or_404(Art.objects.published(), slug=slug )
#    }
#    return render(request,"blog/detail.html",context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Art.objects.published(), slug=slug )


#def category (request , slug ,page=1):
#    category = get_object_or_404(Category, slug=slug ,status=True)
#    article_list = category.articles.published()
#    paginator = Paginator(article_list, 5) 
#    articles = paginator.get_page(page)
#    context = {
#        "category": category,
#        "articles": articles,
#    }
#    return render(request,"blog/category.html",context)

class CategoryList(ListView):
    paginate_by = 5
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug )
        return category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
    
class AuthorList(ListView):
    paginate_by = 5
    template_name = 'blog/author_list.html'

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username )
        return author.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context