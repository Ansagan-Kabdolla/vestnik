from django.shortcuts import render

from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView
from .forms import PdfForm
from .models import *
import os
from django.http import HttpResponse



class PdfCreateView(CreateView):
    model=Filepdf
    template_name = 'publication/add.html'
    form_class = PdfForm
    success_url = '/all_files'

def index(request):
    preds = Predmeti.objects.all()
    return render(request, "publication/zhurnal.html",{'preds':preds})

def show(request):
    ps = Filepdf.objects.all()
    return render(request, "publication/publ.html", {'ps': ps})

def only(request,pk):
    q = get_object_or_404(Filepdf, pk=pk)
    return render(request, 'publication/only.html', {'q': q})

def download(request,fn):
   # fp = open(path, "rb")
   # response = HttpResponse(fp.read())
   # fp.close()
    file = Filepdf.objects.get(file=fn)
    name = file.file
    path_to_file = os.path.realpath("media/{}".format(name))
    f = open(path_to_file, 'rb')
    response = HttpResponse(f, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=' + str(name)
    return response


def predmet(request,pn):
    pred = Predmeti.objects.get(id=pn)
    pred_publ = Filepdf.objects.filter(serius_id=pn)
    return render(request,'publication/predmet.html',{"pred_publ":pred_publ,"pred":pred})

def gid(request):
    preds = Predmeti.objects.all()
    return render(request, "publication/Gid.html",{'preds':preds})


def zhurnal(request):
    preds = Predmeti.objects.all()
    return render(request, 'publication/index.html',{'preds':preds})


def etic(request):
    preds = Predmeti.objects.all()
    return render(request, 'publication/Etic.html',{'preds':preds})

def all_files(request):
    files = Filepdf.objects.all()
    return render(request, 'publication/Pdf_files.html',{'files':files})