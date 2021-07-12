from django.urls import path
from book_outlet import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book/<slug:slug>', views.book_detail, name="detail"),
]
