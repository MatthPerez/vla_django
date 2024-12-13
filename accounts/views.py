from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login, authenticate
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import AddCustomUser, SigninForm
from .models import CustomUser


class Signup(View):
    def get(self, request):
        form = AddCustomUser()

        return render(
            request,
            "accounts/signup.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = AddCustomUser(request.POST)

        if form.is_valid():
            custom_user_data = form.cleaned_data

            custom_user = CustomUser(
                email=custom_user_data["email"],
                password=custom_user_data["password"],
                first_name=custom_user_data["first_name"],
                last_name=custom_user_data["last_name"],
                city=custom_user_data["city"],
            )

            custom_user.save()

            return redirect("index")
        else:
            print(form.errors)

            return render(
                request,
                "accounts/signup.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )


class Signin(LoginView):
    template_name = "accounts/signin.html"
    success_url = reverse_lazy("index")

    def get_success_url(self):
        return self.success_url


class Logout(LogoutView):
    next_page = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        user = request.user

        response = super().get(request, *args, **kwargs)

        if "next" in request.session:
            return HttpResponseRedirect(request.session.pop("next"))

        return response

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("index"))
        return super().dispatch(request, *args, **kwargs)


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None


class Signin(FormView):
    form_class = SigninForm
    template_name = "accounts/signin.html"
    success_url = "/"

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, "Email ou mot de passe incorrect.")
            return self.form_invalid(form)
