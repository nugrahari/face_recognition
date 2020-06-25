from django.shortcuts import render

# Create your views here.
def index(request): 
    context = {
        'Judul' : 'Home',
        'SubJudul' : 'PENGENALAN IDENTITAS BERDASARKAN CITRA WAJAH MENGGUNAKAN METODE LOCAL BINARY PATTERN DAN K-NEAREST NEIGHBOR',
    }
    return render(request, 'home/index.html', context)