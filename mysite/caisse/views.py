from django.shortcuts import render, redirect
from blog.models import Article

# Create your views here.
def caisse(request):
    list_article = {}
    list_key = {}
    
    if request.POST:
        if request.POST.get('barcode') != "":
            try:
                article : Article = Article.objects.get(barcode=request.POST.get('barcode'))
                if 'listkey' in request.session:
                    list_key = request.session.get('listkey')
                
                if str(article.barcode) in list_key:
                    list_key[str(article.barcode)] += 1
                else:
                    list_key[str(article.barcode)] = 1
                    
                for key, value in list_key.items():
                    article = Article.objects.get(barcode=int(key))
                    list_article[str(article.barcode)]=[article,value]
            finally:
                request.session['listkey'] = list_key
                return render(request, 'caisse/caisse.html', {'listarticles': list_article, 'listkeys':list_key})

    if 'listkey' not in request.session:
        request.session['listkey'] = list_key
    else:
        list_key = request.session['listkey']

    try:
        for key, value in list_key.items():
            article = Article.objects.get(barcode=int(key))
            list_article[article.barcode]=[article,value]
    finally:
        return render(request, 'caisse/caisse.html', {'listarticles': list_article, 'listkeys':list_key})

def paiement(request):
    list_key = request.session['listkey']
    request.session['listkey'] = {}
    
    for key, value in list_key.items():
        article : Article() = Article.objects.get(barcode=int(key))
        article.stock -= value
        article.save()
        
    return redirect('caisse')


def retour(request):
    if request.POST:
        codebar = 0 
        nbrarticle = 0
        
        codebar = request.POST.get('barcode')
        nbrarticle = request.POST.get('nbr')
        
        article : Article() = Article.objects.get(barcode=int(codebar))
        article.stock += int(nbrarticle)
        article.save()
        return redirect('caisse')
    return render(request, 'caisse/retour.html', {})
