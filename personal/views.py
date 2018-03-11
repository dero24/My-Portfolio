from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'personal/home.html')

contact_info = ['If you would like to contact me, please email me.','robertfderosa@gmail.com']
args = {'content': contact_info}
    
def contact(request):
    return render(request, 'personal/contact.html', args)
