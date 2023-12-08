from django.urls import path
from .views import title, writers, books, book_info

app_name = 'task_1'

urlpatterns = [
    path('', title, name='title'),
    path('writers/', writers, name='writers'),
    path('books/', books, name='books'),
    path('books/<int:book>/', book_info, name='book_info'),
]
