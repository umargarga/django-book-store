from django.http import Http404
from django.shortcuts import render

from book_outlet.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {'books': books})


def book_detail(request, pid):
    try:
        book = Book.objects.get(pk=pid)
    except:
        raise Http404()

    return render(request, "book_outlet/book_detail.html",
                  {
                      'title': book.title,
                      'author': book.author,
                      'rating': book.rating,
                      'is_bestseller': book.is_bestselling
                  })
