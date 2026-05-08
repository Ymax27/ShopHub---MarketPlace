from django.contrib import admin
from django.urls import path
from item.views import detail, new, delete, edit, items

app_name = 'item'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', items, name='items'),
    path('<int:pk>/', detail, name='detail'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/edit/', edit, name='edit'),
    path('new/', new, name='new'),
]
