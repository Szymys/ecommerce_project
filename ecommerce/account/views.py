from django.shortcuts import render, redirect


from .forms import CreateUserForm, LoginForm, UpdateUserForm

# DO LOGOWANIA
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# KUPOWANIE
from payment.forms import ShippingForm
from payment.models import ShippingAddress


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            form.save()

            # PRZEADRESOWANIE DO APKI STORE czyli wracamy na storne glowna
            return redirect('store')
        


    context = {'form':form}





    return render(request, 'account/registration/register.html', context=context)





def email_verification(request):

        pass



def email_verification_sent(request):

        pass



def email_verification_success(request):

        pass



def email_verification_failed(request):

        pass



# LOGOWANIE
def my_login(request):
      
        form = LoginForm()

        if request.method == 'POST':
            
                form = LoginForm(request, data=request.POST)

                if form.is_valid():

                        username = request.POST.get('username')
                        password = request.POST.get('password')

                        user = authenticate(request, username=username, password=password)

                        if user is not None:
                        
                                auth.login(request, user)

                                return redirect("dashboard")
                        
        context = {'form':form}

        return render(request, 'account/my-login.html', context=context)



# WYLOGOWANIE
def user_logout(request):

        auth.logout(request)

        return redirect("store")



# PANEL
@login_required(login_url='my-login')
def dashboard(request):
       
       return render(request, 'account/dashboard.html')



# ZARZADZANIE KONTEM
@login_required(login_url='my-login')
def profile_management(request):

# AKTUALIZACJA MAILA I NICKU
        if request.method == 'POST':

                user_form = UpdateUserForm(request.POST, instance=request.user)

                if user_form.is_valid():

                        user_form.save()

                        return redirect('dashboard')


        user_form = UpdateUserForm(instance=request.user)

        context = {'user_form':user_form}

        return render(request, 'account/profile-management.html', context=context)



# USUWANIE KONTA
@login_required(login_url='my-login')
def delete_account(request):


        user = User.objects.get(id=request.user.id)

        if request.method == 'POST':
               
               user.delete()

               return redirect('store')


        return render(request, 'account/delete-account.html')


# kupowanie widok
@login_required(login_url='my-login')
def manage_shipping(request):
       
        try:
              
                shipping = ShippingAddress.objects.get(user=request.user.id)


        except ShippingAddress.DoesNotExist:
              
                shipping = None

        form = ShippingForm(instance=shipping)
       

        if request.method == 'POST':
              
                form = ShippingForm(request.POST, instance=shipping)

                if form.is_valid():
                     
                        shipping_user = form.save(commit=False)

                        shipping_user.user = request.user

                        shipping_user.save()

                        return redirect('dashboard')

        context = {'form':form}

        return render(request, 'account/manage-shipping.html', context=context)













