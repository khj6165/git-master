from django.shortcuts import render
from .models import MyUser

# Create your views here.
def create_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        bdate = request.POST.get('bdate')
        MyUser.objects.create(name=name, age=age, bdate=bdate)
    return render(request, 'users/create.html')
    
    
def user_list(request):
    users = MyUser.objects.all()
    return render(request, 'users/user_list.html', {"users: users"})