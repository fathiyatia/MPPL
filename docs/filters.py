import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class DocsFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="tanggal_surat", lookup_expr='gte',label="Sesudah Tanggal")
    end_date = DateFilter(field_name="tanggal_surat", lookup_expr='lte',label="Sebelum Tanggal")
    dari_atau_ke = CharFilter(field_name="dari_atau_ke", lookup_expr='icontains',label="Dari atau ke")
    tempat = CharFilter(field_name="tempat", lookup_expr='icontains',label="Tempat")
    acara = CharFilter(field_name="acara", lookup_expr='icontains',label="Acara")
    keterangan = CharFilter(field_name="keterangan", lookup_expr='icontains',label="Keterangan")
    class Meta: 
        model = Documents
        fields = [
            'dari_atau_ke', 'tempat', 'acara', 
            'keterangan', 'kategori'
        ]