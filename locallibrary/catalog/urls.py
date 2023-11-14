from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail')
]

