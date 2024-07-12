from django.shortcuts import render,redirect
from .models import Recipes
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.


def Display_Recipes(request):
    Recipe = Recipes.objects.all()

    if request.GET.get('search'):
        Recipe = Recipes.objects.filter(descriptions__icontains = request.GET.get('search'))

    return render(request,'home.html',{'Recipes':Recipe})

@login_required(login_url="LogIn")
def Create_Recipe(request):
    if request.method == "POST":

        data = request.POST

        Recipe_name = data.get("recipe_name")
        Recipe_desc = data.get("recipe_desc")
        Recipe_img = request.FILES.get("recipe_img")

        Recipes.objects.create(
            name= Recipe_name,
            descriptions=Recipe_desc,
            image= Recipe_img
        )

        return redirect(Display_Recipes)

    return render(request,'create_recipe_form.html')




@login_required(login_url="LogIn")
def Delete_Recipe(request, recipe_id):
    data = Recipes.objects.get(id=recipe_id)
    data.delete()
    return redirect(Display_Recipes)






@login_required(login_url="LogIn")
def Edit_Recipe(request,recipe_id):
    querySet = Recipes.objects.get(id=recipe_id)

    if request.method == "POST":

        data = request.POST

        Recipe_name = data.get("recipe_name")
        Recipe_desc = data.get("recipe_desc")
        Recipe_img = request.FILES.get("recipe_img")

        querySet.name = Recipe_name
        querySet.descriptions = Recipe_desc

        if Recipe_img:
            querySet.image = Recipe_img
        
        querySet.save()
        return redirect(Display_Recipes)

    return render(request,'edit.html',{'query': querySet})



def Register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request,'Confirm Password Not Match')
            return redirect(Register)

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,'Username Already Exists Select Unique Username')
            return redirect(Register)

        user = User.objects.create(
            username = username,
        )

        user.set_password(password)

        user.save()
        messages.success(request,"Account Created Successfully")
        return redirect(Register)
    return render(request,'auth/register.html')



def LogIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")


        if not User.objects.filter(username = username).exists():
            messages.error(request,'Username Not Found ! ')
            return redirect(LogIn)

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request,'Incorrect Password ! ')

        else:
            login(request,user)
            return redirect(Display_Recipes)
    return render(request,'auth/login.html')


def LogOut(request):
    logout(request)
    return redirect(LogIn)
