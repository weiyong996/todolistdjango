from django.urls import path, include

from .views import ItemListView

urlpatterns = [
    path('', ItemListView.as_view(), name='item-list'),
]