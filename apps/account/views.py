from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from apps.account.forms import CustomErrorList, CustomUserCreationForm


def signup(request):
    template_data = {}
    template_data["title"] = "Sign Up"
    if request.method == "GET":
        template_data["form"] = CustomUserCreationForm()
        return render(request, "account/signup.html", {"template_data": template_data})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect("accounts.login")
        else:
            template_data["form"] = form
            return render(
                request, "account/signup.html", {"template_data": template_data}
            )


def login(request):
    template_data = {}
    template_data["title"] = "Login"
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("home.index")

        return render(request, "account/login.html", {"template_data": template_data})
    elif request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            auth_login(request, user)
            return redirect("home.index")
        else:
            template_data["error"] = "The username or password is incorrect."
            return render(
                request, "account/login.html", {"template_data": template_data}
            )


@login_required
def logout(request):
    auth_logout(request)
    return redirect("home.index")
