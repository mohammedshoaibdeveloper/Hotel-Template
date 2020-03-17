from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'index.html')
def execs(request):

    return render(request,'execs.html')
def contact(request):

    return render(request,'contact.html')