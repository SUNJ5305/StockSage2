from django.urls import path
from . import views


urlpatterns = [
   path("signup/", views.signup, name="signup"),
   path("login/", views.login, name="login"),
   path("logout/", views.logout, name="logout"),
   path("info/", views.info, name="info"),
   path("update/", views.update, name="update"),
   path("chgpass/", views.chgpass, name="chgpass"),
   path("delete/", views.delete, name="delete"),
]