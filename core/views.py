from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')  # Menampilkan template index.html

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Ambil data form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Kirim email
            try:
                send_mail(
                    subject,  # Subjek email
                    message,  # Isi pesan
                    email,    # Pengirim
                    [settings.RECEIVING_EMAIL_ADDRESS],  # Penerima
                    fail_silently=False,
                )
                return HttpResponse('Email berhasil dikirim.')
            except Exception as e:
                return HttpResponse(f'Terjadi kesalahan: {str(e)}')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})