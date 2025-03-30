from django.urls import path
from . import views
from .views import BookUpdateView, BookDeleteView

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-category/', views.add_category, name='add_category'),
    path('book/edit/<int:pk>/', BookUpdateView.as_view(), name='edit_book'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='delete_book'),
    path('categories/', views.category_list, name='category_list'),
    path('category/edit/<int:pk>/', views.CategoryUpdateView.as_view(), name='edit_category'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete_category'),
]