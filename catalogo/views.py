from django.shortcuts import render
from catalogo.models import Book
from catalogo.models import Author
from django.views import generic
# Create your views here.
def indice(request):
    libros = Book.objects.all()
    autores = Author.objects.all()

    datos = {'autores': autores, 'libros': libros}
    
    return render(request, 'index.html', context=datos)

def libros(request):
    libros = Book.objects.all()
    
    datos = {'autor': 'Luis Miguel', 'libros': libros}
    
    return render(request, 'libros.html', context=datos)

def autores(request):
    autores = Author.objects.all()
    
    datos = {'autores': autores, 'libros': libros}
    
    return render(request, 'autores.html', context=datos)

def contacto(request):
    return render(request, 'contacto.html',)

def buscar(request):
    libros = Book.objects.all()
    autores = Author.objects.all()

    datos = {'autores': autores}
    
    busqueda = request.GET.get('q')
    if busqueda:
        libros = Book.objects.filter(title__icontains=busqueda)
        datos['noencontrado'] = True
    else:
        libros = Book.objects.all()
    
    datos['libros'] = libros
    
    return render(request, 'buscar.html', context=datos)

def todos_libros(request):
    libros = Book.objects.all().order_by('title')
    
    datos = {'libros': libros}
    
    return render(request, 'todos_libros.html', context=datos)

class LibrosListView(generic.ListView):
    '''Vista generica para el listado de libros'''
    model = Book
    paginate_by = 10
    
class SearchResultsListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'search_results.html'
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(title__icontains=query)