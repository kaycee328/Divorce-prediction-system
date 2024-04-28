from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# This view handles user sign up authentication
def signupPage(request):
    form = UserRegisterForm()

    if request.method == 'POST': #executes this code block if the form sends a POST request
        form = UserRegisterForm(request.POST)

        if form.is_valid(): #this code block runs if the form values are valid
            form.save()
            return redirect('signin')
        
    context = {'form': form}
    return render(request, 'users_app/auth/signup.html', context)

# This view handles user login authentication
class UserLogin(LoginView):
    template_name = 'users_app/auth/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str: #this is the url that should load when the user successfully logs in
        return reverse_lazy('homepage')

# This view handles user logout
class Logout_user(LogoutView):
    template_name = 'users_app/auth/logout.html'
