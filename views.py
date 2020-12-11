from django.shortcuts import render
from DBRapp.forms import NewBookForm, SearchForm
from DBRapp import models
from DBRapp.models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request, user)
            request.session['username']=username
            return HttpResponseRedirect('/DBRapp/view-books/')
        else:
            data['error']="username or password is incorrect"
            res=render(request,'DBRapp/user_login.html',data)
            return res
    else:
        return render(request,'DBRapp/user_login.html',data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/DBRapp/login/')

@login_required(login_url='DBRapp/login')
def searchBook(request):
    form=SearchForm()
    res=render(request,'DBRapp/search_book.html',{'form':form})
    return res

@login_required(login_url='DBRapp/login')
def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'DBRapp/search_book.html',{'form':form,'books':books})
    return res

@login_required(login_url='DBRapp/login')
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('DBRapp/view-books')

@login_required(login_url='DBRapp/login')
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'DBRapp/edit_book.html',{'form':form,'book':book})
    return res

@login_required(login_url='DBRapp/login')
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('DBRapp/view-books')

@login_required(login_url='DBRapp/login')   #works for viewBooks
def viewBooks(request):
    books=models.Book.objects.all() #objects is single row and objects.all is all rows
    username=request.session['username']
    res=render(request, 'DBRapp/view_book.html', {'books':books,'username':username})
    return res

@login_required(login_url='DBRapp/login')
def newBook(request):
    form=NewBookForm()
    res=render(request,'DBRapp/new_book.html',{'form':form})
    return res

@login_required(login_url='DBRapp/login')
def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()  #object of Book class
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="Record Stored<br><a href='/DBRapp/view-books'> View All Books </a>"
    return HttpResponse(s)
