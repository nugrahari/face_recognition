from django.shortcuts import render ,redirect
from .forms import DatasetForm
from .models import Dataset
from django.core.files.storage import FileSystemStorage
from myWebsite.settings import MEDIA_ROOT

import cv2
import os

from lib.main_function import get_lbpImg
from lib.database import DB
DB.init()
# Create your views here.
def index(request): 
    
    # tb_dataTraining = DB.find('tb_dataTraining')
	tb_dataTraining = Dataset.objects.all()
	# try:
	# 	data = tb_dataTraining[0].lbp_hist
	# 	data = data.split(", ")
	# 	for z in data:
	# 		z = float(z)
	# 		print(type(z))
	# except:
	# 	pass

    # for dt in data:
    # 	print(dt)
    # print(tb_dataTraining[0]['lbp_hist'])

	context = {
        'Judul' : 'Dataset',
        'SubJudul' : 'Berikut dataset yang akan digunakan sebagai data training k-NN',
        'tb_dataTraining' : tb_dataTraining
    }
	return render(request, 'dataset/index.html', context)

def upload(request):

	if request.method == 'POST':

		fs = FileSystemStorage()
		uploaded_file = request.FILES['image']
		label = request.POST['label']

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

		data = ""
		for x in lbp_value:
			if data == "":
				data = str(x)
			else:
				data = data + ", "+ str(x)

		dataTraining = Dataset.objects.create(
			lbp_hist = data,
    		image = name,
		    label = label,
		    directory = directory
		)
		
		return redirect('dataset')

	form = DatasetForm()
	context = {
        'Judul' : 'Tambah Dataset',
        'SubJudul' : 'Tambah Dataset',
        'form'	: form
    }
	return render(request, 'dataset/upload.html', context)



def delete(request, id):
	
	tb_dataTraining = Dataset.objects.get(id = id)
	try:
		# dir_path = os.path.dirname(os.path.realpath(__file__))
		filepath = os.path.join(MEDIA_ROOT,tb_dataTraining.image)
		os.remove(filepath)
	except:
		print('gagal hapus file')
	tb_dataTraining.delete()
	
	return redirect('dataset')
	# return render(request, 'dataset/index.html', context)


from rest_framework import viewsets
from .serializers import LanguageSerializer

class APIView(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = LanguageSerializer