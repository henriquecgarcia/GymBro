from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import GymUserForm

# Create your views here.
def test(request):
	return HttpResponse("Hello, world. You're at the website index.")

def register(request):
    if request.method == 'POST':
        form = GymUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user.user)  # Faz login automaticamente após o registro
            return redirect('home')  # Redireciona para a página inicial após o login
    else:
        form = GymUserForm()
    return render(request, 'register.html', {'form': form})