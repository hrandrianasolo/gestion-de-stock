from django.shortcuts import render, redirect

from blog.models import Provider, Article


def home(request):
    return redirect('provider')

    
def provider(request):
    list_provider = Provider.objects.all().order_by('-name')
    return render(request, 'blog/provider.html', {'listprovider': list_provider})


def article(request):
    list_article = Article.objects.all().order_by('-name')
    return render(request, 'blog/article.html', {'listarticle': list_article})

