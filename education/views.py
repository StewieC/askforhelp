# views.py
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewArticleForm

def index(request):
    # articles = 
    context={
        'articles': Article.objects.all()
    }
    # searchArticle = {
    #     'show_article_search': True
    # }
    return render(request, 'education/index.html', context)

def article_detail(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'education/article_detail.html', {'article': article})

# def search_contacts(request):
#     if request.method == 'POST':
#         location = request.POST.get('location')
#         contacts = Location.objects.filter(name=location)
#         return render(request, 'contacts.html', {'contacts': contacts})

@login_required
def new(request):
    # global form
    form = NewArticleForm(request.POST) # Initialize form outside the if block
    if request.method == 'POST':
        
        # form = NewArticleForm(, request.FILES)

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


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('education:index')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'education/login.html', {'form': form})

  
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:

        form = SignupForm()

    return render(request, 'education/signup.html', {
        'form': form
    })
    
    
    
    # views.py

from django.contrib.auth.models import User

def search(request):
    query = request.GET.get('query', '')
    results = []
    
    if query:
        # Search for articles with a title matching the query or user whose username matches the query
        results = Article.objects.filter(title__icontains=query) | Article.objects.filter(author__username__icontains=query)
    
    return render(request, 'education/search_results.html', {'results': results, 'query': query})


def faq(request):
    return render(request, 'education/faq.html', {'title': 'FAQs'})