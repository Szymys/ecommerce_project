from django.db import models

from django.urls import reverse

class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)


# ZMIANA NAZWY BO INNACZEJ WYSWIETLA CATEGORYS
    class Meta:

        verbose_name_plural = 'categories'

# WYSWIETLA NAZWE A NIE NP. CATEGORY (1)
    def __str__(self):

        return self.name
    
    def get_absolute_url(self):

        return reverse("list-category", args=[self.slug])
    




class Product(models.Model):

    # mozliwosc dodawania kategorii w produktach
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)

    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default = 'un-branded')

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=250)

    price = models.DecimalField(max_digits=4, decimal_places=2)

# PRZENOSI ZDJECIA DO FOLDERU MEDIA 
    image = models.ImageField(upload_to='images/')


    class Meta:

        verbose_name_plural = 'products'


    def __str__(self):

        return self.title


    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])



