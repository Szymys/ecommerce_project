from django.shortcuts import render, redirect


from .forms import CreateUserForm, LoginForm

# DO LOGOWANIA
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout



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




# PANEL
def dashboard(request):
       
       return render(request, 'account/dashboard.html')





