from django.urls import path

from boot import views

app_name = "boot"
urlpatterns = [
    path("base/", views.test),
    path("home/", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about" ),
    path("contact/", views.contact, name="contact"),
    path("inquiry/create/", views.inquiry_create),
    path("login/", views.login, name="login"),
    path("sign-up/", views.sign_up, name="sign_up"),
    path("logout/", views.logout, name="logout"),
    ]

