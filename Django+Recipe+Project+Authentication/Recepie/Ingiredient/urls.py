
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("",views.Display_Recipes,name='Display_Recipes'),
    path("add/",views.Create_Recipe,name='Create_Recipe'),
    path("<int:recipe_id>/delete/",views.Delete_Recipe,name='Delete_Recipe'),
    path("<int:recipe_id>/edit/",views.Edit_Recipe,name='Edit_Recipe'),
    path("register/",views.Register,name="Register"),
    path("login/",views.LogIn,name="LogIn"),
    path("logout/",views.LogOut,name="LogOut"),
    
] 
