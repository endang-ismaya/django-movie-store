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
            return redirect("home.index")
        else:
            template_data["form"] = form
            return render(
                request, "account/signup.html", {"template_data": template_data}
            )
