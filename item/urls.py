from django.urls import path, include

from . import views
app_name = 'item'
urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>', views.detail, name='detail'),
]