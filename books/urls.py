from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('book/<int:id>',views.single_view, name='single_view'),
    path('articles/<slug:slug>',views.articles_view, name='articles_view')
]

