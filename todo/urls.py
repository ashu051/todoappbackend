from django.contrib import admin
from django.urls import path
from todo import views
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('base/',views.basic,name="base"),
    path('delete/<int:id>/',views.delete,name="deletedata"),
    path('<int:id>/',views.update,name="updatedata")
]