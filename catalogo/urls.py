from django.urls import include, path
from catalogo.views import LibrosListView
from catalogo.views import SearchResultsListView
from catalogo.views import crear_autor

urlpatterns = [
    path('listalibros/', LibrosListView.as_view(), name='listado_libros'),
    path('/busqueda', SearchResultsListView.as_view(), name='search_results'),
    path('author/create', crear_autor, name='crear_autor'),
    
]
