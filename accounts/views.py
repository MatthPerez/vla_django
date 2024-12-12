from django.shortcuts import redirect, render
from django.views import View
from accounts.models import CustomUser
from accounts.forms import AddCustomUser


class Signup(View):
    def get(self, request):
        title = "Inscription"
        submit_text = "S'inscrire"
        form = AddCustomUser()

        return render(
            request,
            "accounts/login.html",
            {
                "title": title,
                "submit_text": submit_text,
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
                "accounts/login.html",
                {
                    "form": form,
                    "errors": form.errors,
                },
            )
