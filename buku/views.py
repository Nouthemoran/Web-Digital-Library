
from django.shortcuts import render, redirect, get_object_or_404
from .models import Buku
from .form import BukuForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from ulasanbuku.models import Ulasanbuku
from docx import Document
from io import BytesIO

def Buku_list(request):
    books = Buku.objects.all()
    return render(request, 'list_buku/Admin.html', {'books': books})



def create_Buku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Buku:read')
    else:
        form = BukuForm()
    return render(request, 'form_buku/Admin.html', {'form': form})

def update_Buku(request, bukuid):
    buku = get_object_or_404(Buku, bukuid=bukuid)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('Buku:read')
    else:
        form = BukuForm(instance=buku)
        form.fields['bukuid'].widget = HiddenInput()

    return render(request, 'form_buku/Admin.html', {'form': form})

def delete_Buku(request, bukuid):
    buku = get_object_or_404(Buku, bukuid=bukuid)
    buku.delete()
    return redirect('Buku:read')


def generate_report_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="library_report.pdf"'

    # Create PDF
    p = canvas.Canvas(response, pagesize=letter)
    
    # Judul laporan
    p.drawString(100, 760, "Library Report")
    p.drawString(100, 750, "----------------------------------")
    
    # Jumlah buku
    total_Bukus = Buku.objects.count()
    p.drawString(100, 735, f"Total Bukus: {total_Bukus}")

    # Total kategori buku
    total_categories = Buku.objects.values('kategoriid').distinct().count()
    p.drawString(100, 705, f"Total Categories: {total_categories}")

    # Buku yang paling populer berdasarkan rating
    popular_Bukus = Ulasanbuku.objects.order_by('-rating')[:5]
    p.drawString(100, 670, "Popular Bukus:")
    y_position = 670
    for buku in popular_Bukus:
        p.drawString(190, y_position, f"{buku.bukuid.judul} - Rating: {buku.rating}")
        y_position -= 20

    p.showPage()
    p.save()

    return response
