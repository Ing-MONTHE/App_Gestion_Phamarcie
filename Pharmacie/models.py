from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

#classe pour les produits
class Produit(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    prix = models.IntegerField()
    quantite = models.PositiveIntegerField()
    description = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to="media/")

    def statut_quantite(self):
        #si la quantite est egale a 0, affiche rupture de stock (rouge)
        if self.quantite == 0:
            return f"({self.quantite}) Rupture_Stock"
        
        #Sinon si la quantite est inferieur ou egale a 60, affiche stock faible (Orange)
        elif self.quantite <= 60:
            return f"({self.quantite}) Faible_Stock"

        #si la quantite est superieure a 15, le produit est en stock (vert)
        else:
            return f"({self.quantite}) Stock_suffisant"
        
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_ajout']

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    date_vente = models.DateTimeField(auto_now_add=True)
    quantite = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amont = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.produit

class Facture_Client(models.Model):
    custumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_achat = models.DateTimeField(auto_now_add=True)
    total_amont = models.ForeignKey(Vente, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return f"Le recu de {self.custumer.custumer}"