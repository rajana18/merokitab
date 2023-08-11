from django.shortcuts import render,redirect
from django.urls import reverse
from . import models

# Create your views here.


def listing(request):
     books = models.Book.objects.all()
     return render(request,'list.html',{"books": books})

def delete(request):
      if request.method =='POST':
           id = request.POST['id']

           b1 = models.Book.objects.filter(pk=id)

           print(b1)
         

           return redirect(reverse('books:listing'))
      return render(request,'delete.html')

def add(request):
      if request.method =='POST':
           book_name = request.POST['book_name']
           author_name = request.POST['author_name']
           price = request.POST['price']
           models.Book.objects.create(
                     name=book_name, author=author_name, price=price)


           return redirect(reverse('books:listing'))
      return render(request,'add.html')


def edit(request):
    return render(request,'edit.html')