from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Проверка на None или пустые значения (более безопасно)
        if not name or not phone or not message:
            return render(request, 'contacts.html', {'error': 'Пожалуйста, заполните все поля.'})



        return render(request, 'contact_success.html', {'name': name})

    return render(request, 'contacts.html')