from django.forms import ModelForm
from .models import Filepdf

class PdfForm(ModelForm):
    class Meta:
        model = Filepdf
        fields = ('author', 'file', 'serius')
