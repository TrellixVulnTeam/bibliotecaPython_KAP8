from django.urls import include, path
from catalogo.views import LibrosListView
from catalogo.views import SearchResultsListView

urlpatterns = [
    path('listalibros/', LibrosListView.as_view(), name='listado_libros'),
    path('/busqueda', SearchResultsListView.as_view(), name='search_results'),
]
