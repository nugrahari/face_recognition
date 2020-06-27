from django.shortcuts import render ,redirect
from .forms import DataTestForm
from dataset.models import Dataset
from .models import DataTesting
from django.core.files.storage import FileSystemStorage
from myWebsite.settings import MEDIA_ROOT

import cv2
import os

from lib.main_function import get_lbpImg, get_kNN_clasification
from lib.database import DB

# Create your views here.
def index(request):
	tb_dataTesting = DataTesting.objects.all()

	context = {
        'Judul' 		: 'Form Pengujian',
        'SubJudul' 		: 'Form Pengujian',
        'tb_dataTesting': tb_dataTesting 
    }
	return render(request, 'testing/index.html', context)

def upload(request):

	if request.method == 'POST':

		x_train = []
		y_train = []
		tb_dataTraining = Dataset.objects.all()
		for data in tb_dataTraining:
			y_train.append(data.label)
			fiture = []
			data = data.lbp_hist.split(", ")
			for z in data:
				z = float(z)
				fiture.append(z)
			x_train.append(fiture)



		fs = FileSystemStorage()
		uploaded_file = request.FILES['image']
		nilai_k = int(request.POST['nilai_k'])

		# get file name
		name = fs.save(uploaded_file.name, uploaded_file)
		# get directori
		directory = fs.url(name)
		# get directory OS
		file_name = os.path.join(MEDIA_ROOT,uploaded_file.name)

		# load image
		img = cv2.imread(file_name)
		# get LBP
		lbp_value = get_lbpImg(img, 8, 4)

		hasil = "not yet"
		hasil = get_kNN_clasification(nilai_k, x_train, y_train, lbp_value)

		dataTraining = DataTesting.objects.create(
    		image = name,
		    label = hasil,
		    directory = directory
		)


		form = DataTestForm()

		context = {
	        'Judul' 		: 'Form Pengujian',
	        'SubJudul' 		: 'Form Pengujian',
        	'hasil'			: hasil,
	        'directory'		: directory,
        	'form'	: form
    	}
		return render(request, 'testing/upload.html', context)
		# return redirect('testing/upload')

	form = DataTestForm()
	context = {
        'Judul' : 'Tambah Data Testing',
        'SubJudul' : 'Tambah Data Testing',
        'hasil'	: 'notyet',
	    'directory'		: '/media_dataset/profil.jpg' ,
        'form'	: form
    }
	return render(request, 'testing/upload.html', context)