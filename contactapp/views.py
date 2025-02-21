# from django.shortcuts import render, redirect
# from .forms import ContactForm

# def contact_view(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'contactapp/contact.html', {'form': ContactForm(), 'success': True})
#     else:
#         form = ContactForm()
    
#     return render(request, 'contactapp/contact.html', {'form': form})

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Contact
# from .serializers import ContactSerializer

# @api_view(['POST'])
# def submit_contact(request):
#     serializer = ContactSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'message': 'Contact form submitted successfully!'}, status=201)
#     return Response(serializer.errors, status=400)

# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from .models import Contact
# from .serializers import ContactSerializer

# def home(request):
#     return render(request, 'home.html')

# def contact_submit(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")

#         if name and email and message:
#             contact = Contact(name=name, email=email, message=message)
#             contact.save()
#             return JsonResponse({"success": True})
    
#     return JsonResponse({"success": False})
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import Contact
# from .serializers import ContactSerializer
# from .forms import ContactForm


# def home(request):
#     return render(request, 'home.html')

# def contact_submit(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")
#         image = request.FILES.get("image")  # For file upload (image)
#         pdf = request.FILES.get("pdf")  # For file upload (PDF)

#         if name and email and message:
#             contact = Contact(name=name, email=email, message=message, image=image, pdf=pdf)
#             contact.save()
#             return JsonResponse({"success": True})
    
#     return JsonResponse({"success": False})



from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Contact
from .serializers import ContactSerializer
from django.shortcuts import render, get_object_or_404
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import ContactForm


@api_view(['POST'])
def contact_submit(request):
    if request.method == 'POST':
      
        serializer = ContactSerializer(data=request.data)
        
        if serializer.is_valid():
           
            contact = serializer.save()
          
            return JsonResponse({'success': True, 'pk': contact.pk})
        
        return JsonResponse({'success': False, 'errors': serializer.errors})


def home(request):
    contacts = Contact.objects.all()  
    return render(request, 'home.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)  
    return render(request, 'contact_detail.html', {'contact': contact})


def contact_list(request):
    contacts = Contact.objects.all()  # Fetch all contacts from the database
    return render(request, 'list_contact.html', {'contacts': contacts})



def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contactapp:contact_list')  # Redirect to contact list after editing
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form})

# ✅ Delete Contact
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('contactapp:contact_list')  # Redirect after deleting
    return render(request, 'confirm_delete.html', {'contact': contact})

    


