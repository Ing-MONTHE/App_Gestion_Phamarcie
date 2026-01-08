from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Produit, Categories

class Affichage(ListView):
    # Affichage du template
    template_name = 'home.html'
    # Recuperation des donnees
    queryset = Produit.objects.all()

#fonction ajout des donnees
def ajout_donnees(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prix = request.POST.get('price')
        quantite = request.POST.get('quantite')
        date_expiration = request.POST.get('date_expiration')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category_id = request.POST.get('categorie')

        #Recuperation des categories dans la table en fonction de l'id
        
        category = Categories.objects.get(pk=category_id)
        Savedonnees = Produit(
            name = name,
            category = category,
            prix = prix,
            quantite = quantite,
            date_expiration = date_expiration,
            description = description,
            image = image
        )
        Savedonnees.save()
        return redirect('home')
    else:
        categories = Categories.objects.all()
    return render(request, 'ajout-donnees.html', {'categories': categories})
