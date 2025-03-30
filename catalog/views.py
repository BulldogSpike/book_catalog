from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import UpdateView, DeleteView
from .models import Book, Category
from .forms import BookForm, CategoryForm


def book_list(request):
    books = Book.objects.all()

    # Фильтрация по названию
    title_query = request.GET.get('title')
    if title_query:
        books = books.filter(title__icontains=title_query)

    # Сортировка
    sort_by = request.GET.get('sort', '-created_at')  # По умолчанию сортировка по дате добавления (новые сверху)
    if sort_by not in ['title', '-title', 'created_at', '-created_at', 'updated_at', '-updated_at']:
        sort_by = '-created_at'  # Защита от некорректных параметров

    books = books.order_by(sort_by)

    # Пагинация
    paginator = Paginator(books, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'catalog/book_list.html', {
        'page_obj': page_obj,
        'sort_by': sort_by,
    })


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'catalog/add_book.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = CategoryForm()
    categories = Category.objects.all()
    return render(request, 'catalog/add_category.html', {'form': form, 'categories': categories})


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'catalog/edit_book.html'
    success_url = '/'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'catalog/delete_book.html'
    success_url = '/'


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {'categories': categories})


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/edit_category.html'
    success_url = '/categories/'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalog/delete_category.html'
    success_url = '/categories/'
