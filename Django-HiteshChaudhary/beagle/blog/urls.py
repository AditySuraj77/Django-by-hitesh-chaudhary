from django.urls import path


from . import views

urlpatterns = [
    path('', views.Blog, name="blog"),
    path('<int:blogid>/', views.Blog_description, name="blog_description"),

]