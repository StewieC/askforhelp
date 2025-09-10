from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from .views import signup

app_name = 'loginSystem'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='loginSystem/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='education:index'), name='logout'),
]