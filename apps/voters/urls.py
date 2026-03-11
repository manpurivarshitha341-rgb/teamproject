from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_voter, name="register_voter"),
    path("list/", views.voter_list, name="voter_list"),
]