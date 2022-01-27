from django.urls import path, include
from django.contrib import admin
from blog import views
from portfolio import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  
  path('admin/', admin.site.urls),
  path('', views.home, name='home'),
  path('blog/', include('blog.urls')),
  #path('exchangerate/', include('exchangerate.urls')),
  #path('about/', views.about, name='about'),
  
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
