from django.shortcuts import render
from student.forms import Registration, Login, Exampleform

# Create your views here.
def registration(request):
    #form = Registration(field_order= ['email', 'first_name', 'last_name', 'city'])
    form = Registration()
    return render(request, 'student/registration.html', {'form' : form})

def login(request):
    # form = Login(auto_id= True)
    #form = Login(initial={'email': 'abhi@gmail.com', 'password' : "qwerty"})
    form = Login()
    return render(request, 'student/login.html', {'form' : form})

def example(request):
    form = Exampleform()
    return render(request, 'student/exampleform.html', {'form':form})