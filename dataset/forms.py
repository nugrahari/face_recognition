from django import forms
# from .models import Dataset

class DatasetForm(forms.Form):
	image = forms.FileField()
	label = forms.CharField(
	        label = "Label Image",
	        max_length = 50,
	        widget = forms.TextInput(
	            attrs={
	                'placeholder':'Nama label dari gambar',

	            }
	        )
	    )


# class DocumentForm(forms.ModelForm):
    # class Meta:
    #     model = Dataset
    #     fields = ('image', 'label')