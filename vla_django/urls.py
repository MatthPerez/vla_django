from django.contrib import admin
from django.urls import include, path

from .views import HomeView
from infos.views import InfosView
from accounts.views import Signup, Signin, Logout


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("commandes/", include("commands.urls")),
    path("communication/", include("communication.urls")),
    path("groupes/", include("groups.urls")),
    path("infos/", InfosView.as_view(), name="infos"),
    path("ma_page/", include("private.urls")),
    path("personnes/", include("persons.urls")),
    path("predication/", include("predication.urls")),
    path("publications/", include("publications.urls")),
    path("vcm/", include("vcm.urls")),
    path("we/", include("we.urls")),
    path("inscription/", Signup.as_view(), name="signup"),
    path("connexion/", Signin.as_view(), name="signin"),
    path("deconnexion/", Logout.as_view(), name="logout"),    
]
