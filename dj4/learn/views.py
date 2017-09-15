#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse

def sygp(request):
    return HttpResponse(u'爱你颖儿')

def home(request):
    TutorialList = ["孙颖","刘红芳","刘伟璐","梁瑞","詹"]
    string = u"你真的在乎我吗？"
    return render(request,'home.html',{'string':string,'TutorialList': TutorialList})
# Create your views here.
