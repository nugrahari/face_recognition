from django import forms
# from .models import Dataset

class DataTestForm(forms.Form):
	image = forms.FileField()
	
	nilai_k = forms.IntegerField(required=True)


# class DocumentForm(forms.ModelForm):
    # class Meta:
    #     model = Dataset
    #     fields = ('image', 'label')