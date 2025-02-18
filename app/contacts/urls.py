from django.urls import path

from . import views


urlpatterns = [
    path("<int:contact_id>/", views.list_contact, name="Contact"),
    path("contacts/", views.contacts, name="All Contacts"),
    path("create_contact", views.create_contacts, name="create_contact")
]