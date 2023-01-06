from django.urls import path
from . import views
app_name = "playground"

urlpatterns = [
    path("", views.index, name='index'),
    path('home/', views.home, name="home"),
    path("register/", views.registerPage, name='registration'),
    path("login/", views.loginPage, name='login'),
    path('course/', views.CoursePage, name="course"),
    path('logout/', views.logoutUser, name="logout"),
    # path("<int:post_id>/", views.post_details, name="post-detail"),
]