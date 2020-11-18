from django.http import HttpResponse
from django.shortcuts import render
import joblib
def home(request):
    return render(request,'home.html')
def count(request):
    a=request.GET['a']
    b=request.GET['b']
    li=[]
    li.append(a)
    li.append(b)
    cls=joblib.load('finalized_model.csv')
    ans=cls.predict([li])
    return render(request,'count.html',{'ans':ans})