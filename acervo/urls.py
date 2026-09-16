from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio),
    path("livros/", views.lista_livros, name="lista"),
    path("novo/", views.novo_livro, name="novo_livro"),
    path("disponivel/<int:pk>/toggle", views.update_disponivel, name="toggle_disponivel"),

]
