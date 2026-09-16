from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import LivroForm
from .models import Livro


def inicio(request):
    return HttpResponse("Olá, acervo!")


def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, "acervo/lista.html", {"livros": livros})


def novo_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista")
    else:
        form = LivroForm()

    return render(request, "acervo/form.html", {"form": form})

def update_disponivel(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    livro.disponivel = not livro.disponivel
    livro.save()
    return redirect("lista")