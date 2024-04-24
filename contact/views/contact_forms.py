from django.shortcuts import render, redirect


from contact.models import Contact
from contact.forms import ContactForm

def create(request):
    form = ContactForm(request.POST)

    if request.method == 'POST':
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context,
        )
    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context,
    )