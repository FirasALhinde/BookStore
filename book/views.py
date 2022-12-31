from django.shortcuts import render,redirect,get_object_or_404
from . models import Book
from.forms import BookForm
# Create your views here.

def book_list(request):
    all_book = Book.objects.all()
    context ={'all_book':all_book}
    return render(request,'book/book_list.html',context)


def book_detail(request,id):
    book = get_object_or_404(Book,id=id)
    return render(request,'book/book_detail.html',{'book':book})

def new_book(request):
    if request.method =='POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request,'book/new_book.html',{'form':form})

def edit_book(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method =='POST':
        form = BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
    else:
        form = BookForm(instance=book)
    return render(request,'book/new_book.html',{'form':form})

def delete_book(request,id):
    book = get_object_or_404(Book,id=id)
    book.delete()
    return redirect('/book')