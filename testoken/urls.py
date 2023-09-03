from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('logar', views.logar),
    re_path('registrar', views.registrar),
    re_path('testar', views.testar),
]
