from django.urls import path
from . import views

urlpatterns = [
    path("", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
    path("profile/", views.profile, name="profile"),
    path("profile/update/", views.update_profile, name="update_profile"),
    path("password/change/", views.change_password, name="change_password"),
]