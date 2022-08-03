# from typing_extensions import Required
from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, Staff_form, User_form, Customer_form
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import profile
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def manage_staff(request):
    staff_details = profile.objects.all().filter(staff = True)
    return render(request, 'staffapp/manage_staff.html',
    {'staff':staff_details})

@login_required
def manage_customer(request):
    customer_details = profile.objects.all().filter(staff=False)
    return render(request, 'staffapp/manage_customer.html',
    {'customer':customer_details})

@login_required
def staff_profile(request, user_id):
    profile_details = profile.objects.all().filter(user_id=user_id)
    return render(request, 'staffapp/staff_profile.html',
    {'profile_details':profile_details})

@login_required
def customer_profile(request, user_id):
    profile_details = profile.objects.all().filter(user_id=user_id)
    return render(request, 'customerapp/customer_profile.html', {'profile_details':profile_details})

@login_required
@transaction.atomic
def edit_profile(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(request.POST, instance = user)
        profile_form = Staff_form(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            if profile_form.cleaned_data['staff']:
                user.is_staff = True
            else:
                user.is_staff = False
            particula =profile_form.cleaned_data['particulars']
            identit=profile_form.cleaned_data['means_of_identity']
            passpor = profile_form.cleaned_data['profile_passport']
            user.particulars = particula
            user.profile_passport = passpor
            user.means_of_identity = identit
            user.save()
            messages.success(request, ('your profile was successfully update '))
            staff_profile(request, user_id)
        else:
            messages.error(request, ('please correct the error below..'))   
            return HttpResponsePermanentRedirect(reverse('edit_profile', args=(user_id,)))    
    else:
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(instance = user)
        profile_form = Staff_form(instance=user.profile)
    return render(request, 'staffapp/staff_edit_profile_form.html',{
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
@transaction.atomic
def customer_edit_profile(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(request.POST, instance = user)
        customer_form = Customer_form(request.POST or None, request.FILES  or None, instance = user.profile)
        if user_form.is_valid() and customer_form.is_valid():
            profile_passport = customer_form.cleaned_data['profile_passport']
            user.profile_passport = profile_passport
            user_form.save()
            customer_form.save()
            user.save()
            messages.success(request, ('your profile was successfully update '))
        else:
            messages.error(request, ('please correct the error below..'))   
            return HttpResponsePermanentRedirect(reverse('customer_edit_profile', args=(user_id,))) 
    else:
        user = get_object_or_404(User, id=user_id)
        user_form = User_form(instance = user)
        customer_form = Customer_form(instance=user.profile)
    return render(request, 'customerapp/customer_edit_profile_form.html',{
        'user_form' : user_form,
        'customer_form' : customer_form
    })  


@login_required
def deactivate_staff(request, user_id):
    user = User.objects.get(id = user_id)
    if user.is_active:
        user.is_active = 0
    else:
        user.is_active = 1
    user.save()
    return staff_profile(request, user_id)  