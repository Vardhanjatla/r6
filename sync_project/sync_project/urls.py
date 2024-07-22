from django.contrib import admin
from django.urls import path
from sync_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sync/', views.sync_view, name='sync'),
    path('', views.sync_view, name='home'),  # Root URL pattern
]
