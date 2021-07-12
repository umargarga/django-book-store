from django.db.models import Avg
from django.http import Http404
from django.shortcuts import render

from book_outlet.models import Book


def index(request):
    books = Book.objects.all().order_by("title")
    total_book_count = books.count()
    average_rating = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html",
                  {
                      'books': books,
                      'total_book_count': total_book_count,
                      'average_rating': average_rating
                  })


def book_detail(request, slug):
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()

    return render(request, "book_outlet/book_detail.html",
                  {
                      'title': book.title,
                      'author': book.author,
                      'rating': book.rating,
                      'is_bestseller': book.is_bestselling
                  })
