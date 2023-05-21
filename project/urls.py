from django.contrib import admin
from django.urls import path, include
from newspaper import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('newspaper.urls')),
    path('', views.home, name='home'),
]

