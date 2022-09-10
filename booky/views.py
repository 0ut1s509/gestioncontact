from django.shortcuts import render, redirect
from .models import Contact
from .form import ContactForm
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def add_contact(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            contact=form.save()
            return redirect(list_contact)

        else:
            print('Verifye siw byen ranpli tout chan yo')
    else:
        form=ContactForm()
    context={
        'form':form

    }


    return render(request, 'add-contact.html', context)

def mod_contact(request, non):
    contact=Contact.objects.get(fullname=non)
    print(contact.phone_number)
    
    if request.method == "POST":
        name=request.POST.get('fullname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        adress=request.POST.get('adress')
        website=request.POST.get('website')
        occupation=request.POST.get('occupation')
        company=request.POST.get('company')

        contact.fullname=name
        contact.phone_number=phone
        contact.email=email
        contact.adress=adress
        contact.adress=adress

        if occupation:
            contact.occupation=occupation

        if company:
            contact.company=company

        contact.save()
        return redirect(list_contact)






    context={
        'contact':contact
    }


    return render(request, 'mod_contact.html', context)


def search_contact(request, non):
    contact=Contact.objects.get(fullname=non)
    context={
        'contact':contact
    }

    return render(request, 'search_contact.html', context)

def list_contact(request):
    Lcontact=Contact.objects.all()

    if request.method == 'POST':
        value=request.POST.get('bouton')
        mod=request.POST.get('modify')
        dele=Contact.objects.filter(fullname=value).delete()
        if mod:
            return redirect(mod_contact, non=mod)
      
       
    context={
        'Lcontact':Lcontact
    }

    return render(request, 'list_contact.html', context)

def search(request):
    context={}
    if request.method == 'POST':
        value=request.POST.get('fullname')
        if Contact.objects.filter(fullname=value):
            return redirect(search_contact, non=value)
        else:
            unexist=1

            context={
                'unexist':unexist
                }
    return render(request, "rech.html", context)



