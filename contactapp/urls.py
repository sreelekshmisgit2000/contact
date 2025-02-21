

from django.urls import path
from . import views

app_name = "contactapp"

urlpatterns = [
    path('', views.home, name='home'),  
    path('submit/', views.contact_submit, name='contact_submit'),
    path('contact/view/<int:pk>/', views.contact_detail, name='contact_detail'), 
    path('contacts/',views.contact_list, name='contact_list'),
    path('contact/<int:pk>/edit/', views.edit_contact, name='edit_contact'),
    path('contact/<int:pk>/delete/', views.delete_contact, name='delete_contact'),
]
