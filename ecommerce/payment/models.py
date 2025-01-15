from django.db import models

from django.contrib.auth.models import User


class ShippingAddress(models.Model):

    full_name = models.CharField(max_length=300)

    email = models.EmailField(max_length=300)
    
    address1 = models.CharField(max_length=300)
    
    address2 = models.CharField(max_length=300)

    city = models.CharField(max_length=300)

    zipcode = models.CharField(max_length=300)

    # NIEWYMAGANE
    state = models.CharField(max_length=300, null=True, blank=True)

    # wiele od jednego(jeden user wiele adresow), jak zostanie usuniety to adresy tez
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)




class Meta:

    verbose_name_plural = 'Shipping Address'



def __str__(self):

    return 'Shipping Address - ' + str(self.id)




















