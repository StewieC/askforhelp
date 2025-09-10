from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewArticleForm

def index(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'education/index.html', context)

def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'education/article_detail.html', {'article': article})

@login_required
def new(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('education:index')
    else:
        form = NewArticleForm()
    return render(request, 'education/article_form.html', {
        'form': form,
        'title': 'New Article',
    })

def search(request):
    query = request.GET.get('query', '')
    results = []
    if query:
        results = Article.objects.filter(Q(title__icontains=query) | Q(author__username__icontains=query))
    return render(request, 'education/search_results.html', {'results': results, 'query': query})

def faq(request):
    return render(request, 'education/faq.html', {'title': 'FAQs'})