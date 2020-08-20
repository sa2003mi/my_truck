from django.shortcuts import render, redirect, get_object_or_404, Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from .forms import SignUpForm , UserForm ,ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy , reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.utils.translation import ugettext, activate,get_language


# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('service:index')
    else:
        if request.method == 'POST' :
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request,user)
                return redirect('service:index')
        else:
            form = SignUpForm()


        return render(request,'signup.html',{'form':form})


###########################################################
# This area for trying




# End area trying
#########################################################################3
def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_profile = profile_form.save(commit=False)
            my_profile.user = request.user
            my_profile.save()
            messages.success(request, 'Your profile edit successfully.')
            return redirect(reverse('accounts:profile'))

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        

    }
    return render(request, 'edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/accounts/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
