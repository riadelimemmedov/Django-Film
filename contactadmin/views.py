from django.shortcuts import render
from .models import *
from profiles.models import *

# Create your views here.
def contactView(request):
    profile = Profile.objects.get(user=request.user)
    contactprof = ContactModel.objects.get(contact_prof=profile)
    
    if request.method == 'POST':
        print('POST ATILDI CONTACT')
        print(request.POST.get('salamcontact'))
    
    print('Writing Profile First Name',contactprof.contact_prof.user.first_name)
    print('Writing Profile Last Name',contactprof.contact_prof.user.last_name)
    print('Writing Profile Email',contactprof.contact_prof.user.email)
    print('Writing Profile Text',contactprof.contact_message)
    
    
    context = {
        'qs':'Hello Contact Page'
    }
    
    return render(request,'contactadmin/contact.html',context)