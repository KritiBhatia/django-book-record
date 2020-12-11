from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee

def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/employees.html',data)
    return(res)
def greeting(request):
    s="<h1> Hello, I'm learning Django </h1><p> This is landing page</p>"
    return HttpResponse(s)
def showContact(request):
    s='<h1>This is the contact page</h1>'
    s+="<p>E-mail: xyz@gmail.com"
    s+="<p>Ph.No: 8182838485 "
    s+="<a href='#'>My website</a>"
    return HttpResponse(s)
def about(request):
 msg="This is an about page, yipee"
 mylist=[10,20,30]
 num=26
 return render(request, 'testapp/about.html',{'msg':msg,'L1':mylist,'num':num})
