from django.forms import ModelForm
from .models import Documents

class DocsForms(ModelForm):
    class Meta:
        model = Documents
        fields = [
            'tanggal_terima', 'dari_atau_ke', 'no_surat', 
            'tanggal_surat', 'hari_jam', 'tempat', 'acara', 
            'keterangan', 'kategori', 'uploaded_file'
        ]
        