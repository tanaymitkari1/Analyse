from django.urls import path
from .views import *


urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('add_new/', add_company, name="add"),
    path('details/', details, name="details"),
    path('login/', user_login, name="user_login"),
    path('logout/', user_logout, name="user_logout"),
    path('register/', user_register, name="user_register"),
    path('<int:id>/details', details, name="details"),
]