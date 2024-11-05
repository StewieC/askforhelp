from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'education'

urlpatterns = [
    path('', views.index, name='index'),
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
    path('new/', views.new, name='new'),
     path('search/', views.search, name='search'),
     path('faq/', views.faq, name='faq'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='education/login.html', authentication_form=LoginForm), name='login'),
]
