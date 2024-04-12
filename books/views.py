from django.shortcuts import render
from .models import Book,Articles
# Create your views here.


def base(request):
    return render(request, 'base.html')

def home(request):
    books = Book.objects.all()
    articles = Articles.objects.all()
    context = {
        'books': books,
        'articles': articles
    }
    return render(request, 'books/home.html', context=context)

def single_view(request,id):
    book = Book.objects.get(id=id)
    context = {
        'book': book,
    }
    return render(request, 'books/slug_view.html', context=context)






# Articles Views

def articles_view(request,slug):
    article = Articles.objects.get(slug=slug)
    context = {
        'article': article
    }
    return render(request, 'articles/articles.html', context)