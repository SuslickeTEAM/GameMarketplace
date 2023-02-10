from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout



def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "auth/signup.html", {"form": form})


class LoginView(BaseLoginView):
    template_name = "Auth/login.html"
    redirect_authenticated_user = True
    


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')



login = LoginView.as_view()

