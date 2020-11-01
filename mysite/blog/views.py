from django.http.response import HttpResponseRedirect
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


def edit_provider(request, provide_id):
    current_provider = Provider.objects.get(id=provide_id)
    if request.POST:
        if request.POST.get('name') != "":
            current_provider.name = request.POST.get('name')
        if request.POST.get('address') != "":
            current_provider.address = request.POST.get('address')
        if request.POST.get('zip_code') != "":
            current_provider.zip_code = request.POST.get('zip_code')
        if request.POST.get('phone') != "":
            current_provider.phone = request.POST.get('phone')

        current_provider.save()
        return HttpResponseRedirect("/provider")
    else:
        return render(request, 'blog/edit_provider.html', {'provider': current_provider})


def edit_article(request, article_id):
    current_article = Article.objects.get(id=article_id)
    list_provider = Provider.objects.all().order_by('-name')
    if request.POST:
        if request.POST.get('name') != "":
            current_article.name = request.POST.get('name')
        if request.POST.get('price') != "":
            current_article.price = request.POST.get('price')
        if request.POST.get('barcode') != "":
            current_article.barcode = request.POST.get('barcode')
        if request.POST.get('stock') != "":
            current_article.stock = request.POST.get('stock')
        if request.POST.get('seuil') != "":
            current_article.seuil = request.POST.get('seuil')
        if request.POST.get('is_sold_with_weight') != "":
            current_article.is_sold_with_weight = request.POST.get('is_sold_with_weight')
        if request.POST.get('provider') != "":
            current_article.provider = Provider.objects.get(id=request.POST.get('provider'))

        current_article.save()
        return HttpResponseRedirect("/article")
    else:
        return render(request, 'blog/edit_article.html', {'article': current_article, 'list_provider': list_provider})


def delete_provider(request, provide_id):
    Provider.objects.get(id=provide_id).delete()
    return HttpResponseRedirect("/provider")


def delete_article(request, article_id):
    Article.objects.get(id=article_id).delete()
    return HttpResponseRedirect("/article")
