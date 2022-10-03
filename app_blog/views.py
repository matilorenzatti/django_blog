
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app_blog.models import Avatar, Post
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from app_blog.forms import AvatarFormulario, UserUpdateForm, RegistroFormulario
from django.contrib.auth.models import User


class Home(TemplateView):
    template_name = "post_list.html"

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("list_posts")
    fields = ["titulo", "subtitulo", "cuerpo", "imagen", "usuario"]

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("list_posts")
    fields = ["titulo", "subtitulo", "cuerpo","imagen", "usuario"]
    template_name = "app_blog/update_form.html"

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("list_posts")

class PostListUser(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post_usuarios.html"


def registro(request):
    mensaje = ""

    if request.method == "POST":
        form = RegistroFormulario(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "app_blog/post_list.html", {"mensaje" : "Usuario creado con éxito."})
        else:
            mensaje = "Cometiste un error en el registro. Revisar."
            context = {"mensaje": mensaje}

    else:
        form = RegistroFormulario()
        context = {"form":form}

    return render(request, "app_blog/registro.html", context)


def login_request(request):
    next_url = "list_posts"

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contra)

            if user:
                login(request, user)
                if next_url:
                    return redirect(reverse_lazy(next_url))
                return render(request, "app_blog/post_list.html", {"mensaje" : f"Bienvenido {usuario}"})
            else:
                return render(request, "app_blog/post_list.html", {"mensaje" : "Error, datos incorrectos"})
        else:
            return render(request, "app_blog/post_list.html", {"mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, "app_blog/login.html", {"form":form})

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "app_blog/logout.html"

@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid:
            try:
                avatar = form.save()
                avatar.user = request.user
                avatar.save()
                return redirect(reverse_lazy('list_posts'))
            except:
                return render(request, 'app_blog/post_list.html', {"mensaje":"Error, ya existe un avatar asociado al usuario"})
            
    form = AvatarFormulario()
    return render(request, "app_blog/form_avatar.html", {"form":form})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("list_posts")
    template_name = "app_blog/form_perfil.html"

    def get_object(self, queryset = None):
        return self.request.user

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'app_blog/form_perfil.html'
    fields = ["password1", "password2"]
    success_url = reverse_lazy("list_posts")

class About(TemplateView):
    template_name = "about.html"