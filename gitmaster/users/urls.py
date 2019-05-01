from django.urls import path
from . import views


urlpatterns = [
    path('user_list/', views.user_list, name="user_list"),
    path('update_user/<int:id>/', views.update_user, name="update_user")
    path('delete_user/<int:id>/', views.delete_user, name="delete_user")
   ]