from django.shortcuts import render
from .models import *
from profiles.models import *

# Create your views here.
def contactView(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        contact_message = request.POST.get('contact_message')
        obj = ContactModel(contact_prof=profile,contact_message=contact_message)
        obj.save()
        
    
    context = {
        'profile':profile,
    }
    
    return render(request,'contactadmin/contact.html',context)