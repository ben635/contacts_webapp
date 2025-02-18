from django.shortcuts import render
from django.http import Http404
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Contact

def list_contact(request, contact_id):
    response = "The name of this contact is %s"
    try:
        return HttpResponse(response % Contact.objects.get(pk=contact_id))
    except Contact.DoesNotExist:
        raise Http404("Contact does not exist.")

def contacts(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, "contacts/index.html", context)

def create_contacts(request):
    newContact = Contact(name=request.POST["name"], address=request.POST["address"], telephone_number=request.POST["telephone_number"])

    newContact.save()

    return HttpResponseRedirect(reverse("Contact", args=(newContact.id,)))