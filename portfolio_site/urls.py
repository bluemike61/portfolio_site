from django.urls import path, include
from django.contrib import admin
from quote_generator import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', views.index, name='index'),
  path('admin/', admin.site.urls),
  #path('',views.home, name='home')
  #path('about/', views.about, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
