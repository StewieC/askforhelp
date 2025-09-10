from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('education.urls', 'education'), namespace='education')),
    path('contacts/', include('contacts.urls')),
    path('inbox/', include('conversation.urls')),
    path('', include(('loginSystem.urls', 'loginSystem'), namespace='loginSystem')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)