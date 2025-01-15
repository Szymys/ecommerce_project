from django.shortcuts import render


# zamowione 
def payment_success(request):

    return render(request, 'payment/payment-success.html')



# blad zamowienia
def payment_failed(request):

    return render(request, 'payment/payment-failed.html')




























