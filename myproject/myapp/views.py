# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Django!")
from django.shortcuts import render
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students':students})
    # return render(request, 'home.html')
