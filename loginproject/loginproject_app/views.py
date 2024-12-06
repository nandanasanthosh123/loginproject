from django.shortcuts import render, redirect
from django.contrib import messages
from .models import LoginDetails
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

# Create your views here.


def home(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')

def registerperson(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile-number')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, _("Passwords do not match."))
            return render(request, 'register.html')

        # Create a new user
        try:
            user = LoginDetails.objects.create(
                name=name,
                email=email,
                mobilenumber=mobile_number,
                username=username,
                password=password  # Note: Store hashed passwords in production
            )
            user.save()
            messages.success(request, _("Registration successful!"))
            return redirect('login')  # Redirect to login page or another page
        except ValidationError as e:
            messages.error(request, e.messages)
        except Exception as e:
            messages.error(request, _("An error occurred: ") + str(e))

    return render(request, 'register.html')