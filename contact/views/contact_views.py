from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from contact.models import Contact

def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')[0:10]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - ',
    }

    return render(
        request,
        'contact/index.html',
        context,
    )

def search(request):
    search_value = request.GET.get('q', '').strip() # get the text in the search, if doesn't, get nothing

    if search_value == '':
        return redirect('contact:index')


    contacts = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id') # icontains check if the value is in the text (case-insensitive)

    context = {
        'contacts': contacts,
        'site_title': 'Search - ',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contact/contact.html',
        context,
    )

