from django.shortcuts import render,redirect
from . models import Book

# Create your views here.
def main(request):
    book = Book.objects.all()
    return render(request, 'main.html', {'book':book})

def add(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        author = request.POST.get('author')
        year = request.POST.get('year')

        a = Book(name=name, author=author, Year=year)
        a.save()

        return redirect(main)
    return render(request, 'Add.html')

def delete(request, id) :
    book = Book.objects.get(id=id)
    book.delete()

    return redirect(main)

    return render(request, 'delete.html', {'book':book})

def update(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.name = request.POST.get('name')
        book.author = request.POST.get('author')
        book.year = request.POST.get('year')

        book.save()

        return redirect(main)
    
    else:
        return render(request, 'update.html', {'book':book})
    

def show(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'show.html', {'book':book})