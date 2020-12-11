from django.shortcuts import render
from django.http import HttpResponse

def showTest(request):
    que="Who developed C language?"
    a="Ken Thompson"
    b="Dennis Ritchie"
    c="James Gosling"
    d="Guido Rossum"
    level="Easy"
    data={'que':que,'a':a,'b':b,'c':c,'d':d,'level':level}
    res=render(request,'exam/test.html',context=data)
    return res
def showResult(request):
    s='<h1> This is showResult page</h1>'
    return HttpResponse(s)
