from .views import SingleCardSearch, FullDeckSearch
from django.urls import path, include

urlpatterns = [
    path('search', SingleCardSearch.as_view(), name='api-search'),
    path('decklist', FullDeckSearch.as_view(), name='api-decklist')
]