from django.shortcuts import render, redirect


def title(request, *args, **kwargs):
    return render(request, 'task_1/title.html')

def writers(request, *args, **kwargs):
    return render(request, 'task_1/writers.html')

def books(request):
    return render(request, 'task_1/books.html')

def book_info(request, book):
    if book == 1:
        return render(request, 'task_1/book_1.html')
    elif book == 3:
        return render(request, 'task_1/book_3.html')
    else:
        return redirect('task_1:books')
