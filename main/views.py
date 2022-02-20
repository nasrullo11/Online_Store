from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from main.models import Product, Racing_boot, Shoes_collection

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        msg = '''
        New message: {} \n
        From: {}\n
        name: {}\n
        phone: {}
        '''.format(message, email, name, phone)
        send_mail('new email', msg, 'from testing email', [email], fail_silently=False)

    shoes_categories = Shoes_collection.objects.all()
    racing_boots = Racing_boot.objects.all()
    shoes = Product.objects.all()
    return render(request, 'index.html', {
        'shoes_categories': shoes_categories,
        'racing_boots': racing_boots,
        'shoes': shoes
    })