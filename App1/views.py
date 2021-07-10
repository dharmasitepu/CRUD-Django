from django.shortcuts import render,redirect
from .forms import mahaform
from .models import maha

# Create your views here.
def maha_list(request):
    context = {'maha_list':maha.objects.all()}
    return render(request,"App1/maha_list.html", context)

def maha_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = mahaform()
        else:
            mahasiswa = maha.objects.get(pk=id)
            form = mahaform(instance=mahasiswa)
        return render(request,"App1/maha_form.html", {'form':form})
    else:
        if id == 0:
            form = mahaform(request.POST)
        else:
            mahasiswa = maha.objects.get(pk=id)
            form = mahaform(request.POST,instance=mahasiswa)
        if form.is_valid():
            form.save()
        return redirect('/mahasiswa/list')

def maha_delete(request,id):
    mahasiswa = maha.objects.get(pk=id)
    mahasiswa.delete()
    return redirect('/mahasiswa/list')