from django.shortcuts import render
from django.http import Http404
from django.urls import reverse

from rest_framework import viewsets

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Contact
from .serializers import ContactSerializer
from django.http import JsonResponse

def list_contact(request, contact_id):
    response = "The name of this contact is %s"
    try:
        return HttpResponse(response % Contact.objects.get(pk=contact_id))
    except Contact.DoesNotExist:
        raise Http404("Contact does not exist.")
    
def delete_contact(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id)
        contact.delete()
        return HttpResponse("Success!")
    except Contact.DoesNotExist:
        raise Http404("Contact does not exist.")

def contacts(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, "contacts/index.html", context)

def create_contacts(request):
    newContact = Contact(
        name=request.POST["name"],
        address=request.POST["address"],
        telephone_number=request.POST["telephone_number"]
    )
    newContact.save()

    data = {
        "success": True,
        "contact": {
            "id": newContact.id,
            "name": newContact.name,
            "address": newContact.address,
            "telephone_number": str(newContact.telephone_number),
        }
    }
    return JsonResponse(data)

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contacts to be viewed or edited
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer