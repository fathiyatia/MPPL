import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class DocsFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="tanggal_surat", lookup_expr='gte')
    end_date = DateFilter(field_name="tanggal_surat", lookup_expr='lte')
    dari_atau_ke = CharFilter(field_name="dari_atau_ke", lookup_expr='icontains')
    tempat = CharFilter(field_name="tempat", lookup_expr='icontains')
    acara = CharFilter(field_name="acara", lookup_expr='icontains')
    keterangan = CharFilter(field_name="keterangan", lookup_expr='icontains')
    class Meta: 
        model = Documents
        fields = [
            'dari_atau_ke', 'tempat', 'acara', 
            'keterangan', 'kategori'
        ]