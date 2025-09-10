from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('', views.index, name='index'),
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),
    path('new/', views.new, name='new'),
    path('search/', views.search, name='search'),
    path('faq/', views.faq, name='faq'),
]