from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from .forms import userRegistrationForm,userUpdateForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required

def registration(request):

    form = userRegistrationForm()

    if request.method == 'POST':

        form = userRegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data['username']

            messages.success(request, f'{username} has been created')

            return redirect('users:index')

    else:

        form = userRegistrationForm()


    return render(request,'account/registration-form.html',{'form':form})


@login_required
def userProfile(request):

    return render(request, 'account/user-profile.html')

@login_required
def userUpdate(request):

    user_form = userUpdateForm()

    if request.method == 'POST':

        user_form = userUpdateForm(request.POST,instance=request.user)

        if user_form.is_valid():

            user_form.save()

            username = user_form.cleaned_data['username']

            messages.success(request, f'{username} account has been updated')

            return redirect('profile:user-profile')

    else:

        user_form = userUpdateForm(instance=request.user)


    return render(request,'account/user-update-form.html',{'user_form':user_form})