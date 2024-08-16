from .views import SingleCardSearch
from django.urls import path, include

urlpatterns = [
    path('search', SingleCardSearch.as_view(), name='api-search')
]