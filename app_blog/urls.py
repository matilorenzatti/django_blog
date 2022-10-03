from django.contrib import admin
from django.urls import path
from app_blog import views

urlpatterns = [
    path("", views.Home.as_view(), name="principal"),
    path("pages/", views.PostList.as_view(), name="list_posts"),
    path("pages/<pk>/", views.PostDetail.as_view(), name="detail_post"),
    path("create_post/", views.PostCreate.as_view(), name="create_post"),
    path("update_post/<pk>/", views.PostUpdate.as_view(), name="update_post"),
    path("delete_post/<pk>/", views.PostDelete.as_view(), name="delete_post"),
    path("users_posts/", views.PostListUser.as_view(), name="users_posts"),
    path("registro/", views.registro, name="registro"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("create_avatar/", views.agregar_avatar, name="create_avatar"),
    path("update_user/", views.ProfileUpdateView.as_view(), name="update_user"),
    path("update_password/", views.PasswordChange.as_view(), name="update_password"),
    path("about/", views.About.as_view(), name="about"),
]
