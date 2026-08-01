from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# ---------------- SIGNUP ----------------

def signup(request):

    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("signup")

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password1,
        )

        messages.success(request, "Signup Successful")
        return redirect("signin")

    return render(request, "signup.html")


# ---------------- SIGNIN ----------------

def signin(request):

    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:

            auth_login(request, user)
            return redirect("profile")

        messages.error(request, "Invalid Username or Password")

    return render(request, "signin.html")


# ---------------- SIGNOUT ----------------

@login_required
def signout(request):

    auth_logout(request)

    return redirect("signin")


# ---------------- PROFILE ----------------

@login_required
def profile(request):

    return render(request, "profile.html")


# ---------------- UPDATE PROFILE ----------------

@login_required
def update_profile(request):

    user = request.user

    if request.method == "POST":

        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        user.username = request.POST["username"]

        user.save()

        messages.success(request, "Profile Updated")

        return redirect("profile")

    return render(request, "update_profile.html", {"user": user})


# ---------------- CHANGE PASSWORD ----------------

@login_required
def change_password(request):

    if request.method == "POST":

        old_password = request.POST["old_password"]

        new_password1 = request.POST["new_password1"]

        new_password2 = request.POST["new_password2"]

        if not request.user.check_password(old_password):

            messages.error(request, "Old password incorrect")

            return redirect("change_password")

        if new_password1 != new_password2:

            messages.error(request, "Passwords do not match")

            return redirect("change_password")

        request.user.set_password(new_password1)

        request.user.save()

        update_session_auth_hash(request, request.user)

        messages.success(request, "Password Changed Successfully")

        return redirect("profile")

    return render(request, "change_password.html")