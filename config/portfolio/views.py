from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from .models import Message

def index(request):
    return render(request, 'index.html')

def about(request):
    author = {
        'name': 'Shashwat',
        'lastname': 'Srivastava'
    }
    return render(request, 'about.html', {'author': author})

def contact(request):
    if request.method == 'POST':
        msg = Message(
            name=request.POST['name'],  
            email=request.POST['email'],
            subject=request.POST['subject'],  
            message=request.POST['message']
         )
        msg.save()
        messages.success(request, 'Message sent!')
        return redirect('contact') 
  
    return render(request, 'contact.html')

def resume_view(request):
    pdf_file = open('media/pdfs/resume.pdf', ' rb')
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    return response