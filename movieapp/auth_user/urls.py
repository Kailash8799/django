from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('forgot/',views.forgot,name="forgot"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('logout/',views.logout,name="logout"),
]
