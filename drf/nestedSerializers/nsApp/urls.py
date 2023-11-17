from django.urls import path
from nsApp import views
from nsApp.views import AuthorListView, AuthorBookListView, AuthorDetailView, BookListView, BookDetailView

urlpatterns = [
    path('author/', AuthorListView.as_view()),
    path('author/<int:pk>', AuthorDetailView.as_view()),
    path('book/', BookListView.as_view()),
    path('book/<int:pk>', BookDetailView.as_view()),
    path('authorbook/', AuthorBookListView.as_view())
]