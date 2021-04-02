from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("offers", views.offers, name="offers"),
    path("tours", views.hot_tours, name="hot_tours"),
    path("blog/<int:blog_id>", views.blogdetails, name="blogdetails"),
    path("blog/<str:categories>", views.category, name="category"),
    path("post", views.add_post, name="post"),
    path("register", views.register, name="register"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("profile", views.profile, name="profile"),
    path("offers/<int:counrty_id>", views.country, name="country"),
    path("search", views.search, name="search"),
    path("booking/<str:title>", views.booking, name="booking"),
    path("checkout", views.checkout, name="checkout"),   

]