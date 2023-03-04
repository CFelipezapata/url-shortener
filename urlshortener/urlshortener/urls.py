from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shorten, name='shorten'),
    path('<str:short_code>', views.redirect_short_url, name='redirect_short_url')
]
