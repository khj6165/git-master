from django.shortcuts import render, redirect, get_object_or_404
from .models import MyUser

# Create your views here.
def create_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        bdate = request.POST.get('bdate')
        MyUser.objects.create(name=name, age=age, bdate=bdate)
        return redirect('user_list')
    return render(request, 'users/create.html')
    
    
def user_list(request):
    users = MyUser.objects.all()
    return render(request, 'users/user_list.html', {'users': users})
    
def update_user(request, id):
    user = get_object_or_404(MyUser, pk=id)
    if request.method=="POST":        
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.bdate = request.POST.get('bdate')
        user.save()
        return redirect('user_list')
    return render(request, 'users/update_user.html', {'user': user})
    
    
def delete_user(request, id):
    user = get_object_or_404(MyUser, pk=id)
    if request.method=="POST":
        return redirect('user_list')