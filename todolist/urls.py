from django.urls import path, include

from .views import ItemListView, ItemDetailView

urlpatterns = [
    path('item/', ItemListView.as_view(), name='item-list'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item-detail'),
]