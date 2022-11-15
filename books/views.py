from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q


# Create your views here.
class BookListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/books_detail.html'

class SearchResultListView(ListView):
    model = Book
    content_object_name = 'book_list'
    template_name = 'books/search_result.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title_icontains=query) | Q(author_icontains=query))
    