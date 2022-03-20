from django.shortcuts import render

# Create your views here.
def contactView(request):
    print('Contact Seyfesi Isledi')
    
    context = {
        'qs':'Hello Contact Page'
    }
    
    return render(request,'contactadmin/contact.html',context)