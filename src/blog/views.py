from django.shortcuts import render

from django.views.generic import  DetailView
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from  django.shortcuts import redirect
from .forms import ProfileForm
from .models import UserProfile
def Dashboard(request):
    template_name='blog/profile.html'
    form = ProfileForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = ProfileForm()
    profile=UserProfile.objects.get(user=request.user)
    context = {
        'picform': form,
        'user_profile':profile,
        }
    return render(request,template_name,context)

def Home(request):
    template_name='blog/home.html'
    return render(request,template_name)