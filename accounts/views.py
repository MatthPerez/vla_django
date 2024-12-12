from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm


class Register(View):
    def get(self, request):
        form = CustomUserCreationForm(request.POST)
        
        return render(
            request,
            "registration/register.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect("login")
