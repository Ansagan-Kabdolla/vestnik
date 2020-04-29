from django.urls import path
from .views import *


urlpatterns = [
    path('', zhurnal),
    path('p/', show),
    path('p/<int:pk>/', only, name='only'),
    path('document/<fn>', download, name='down'),
 #   path('contacts', contact, name='contact'),
    path('gid', gid, name='gid'),
    path('zhurnal', zhurnal, name='zhurnal'),
    path('etic', etic, name='etic'),
    path('predmet/<int:pn>', predmet, name='predmet'),
    path('add/',PdfCreateView.as_view(), name='add'),
    path('all_files/',all_files,name='all_files')
]