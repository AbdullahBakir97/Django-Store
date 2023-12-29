from django.shortcuts import render , redirect
from .models import Profile
from .forms import SignupForm , ActivateForm
from django.core.mail import send_mail
from django.contrib.auth.models import User


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
           username = form.cleaned_data['username']
           email = form.cleaned_data['email']

           # create User(inactive) ------> create Profile [code]
           user = form.save(commit=False)   
           user.is_active = False
           form.save()

           # email code
           profile = Profile.objects.get(user__username=username)

           # send mail
           send_mail(
                "Activate Your Account",
                f"Welcome {username} \nUse this code {profile.code} to activate your account\nMystro Team",
                "abdullah.bakir.204@gmail.com", # send from 
                [email], # send to
                fail_silently=False,
            )
        return redirect(f'/accounts/{username}/activate')
    else:
        form = SignupForm()

    return render(request,'accounts/signup.html',{'form':form})

    # signup ----> code:email ----> activate:code ----> login (activated)

def activate(request,username):
    profile = Profile.objects.get(user__username=username)

    if request.method == 'POST':
        form = ActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''
                profile.save()

                user = User.objects.get(username=username)
                user.is_active = True
                user.save()
                return redirect('/accounts/login')
    else:
        form = ActivateForm()

    return render(request,'accounts/activate.html',{'form':form})