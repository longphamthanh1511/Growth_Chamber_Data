from django.shortcuts import render
from CRUDOperation.models import Plants
from django.contrib import messages
from CRUDOperation.forms import plantforms

def ShowPlants(request):
    showall=Plants.objects.all()
    return render(request, 'Index.html',{"data":showall})

def AddPlants(request):
    if request.method=="POST":
        if request.POST.get('kigo') and request.POST.get('temp') and request.POST.get('hum') and request.POST.get('sun') and request.POST.get('co2') and request.POST.get('water') and request.POST.get('time'):
            AddedPlant=Plants()
            AddedPlant.kigo=request.POST.get('kigo')
            AddedPlant.temp=request.POST.get('temp')
            AddedPlant.hum=request.POST.get('hum')
            AddedPlant.sun=request.POST.get('sun')
            AddedPlant.co2=request.POST.get('co2')
            AddedPlant.water=request.POST.get('water')
            AddedPlant.time=request.POST.get('time')
            AddedPlant.save()
            messages.success(request, ' Plant ' + AddedPlant.kigo+ ' Added ')
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')
    
def DataChange(request,id):
    ChangeData=Plants.objects.get(id=id)
    return render(request, 'edit.html',{"Plants":ChangeData})

def DataUpdate(request,id):
    UpdateData=Plants.objects.get(id=id)
    form=plantforms(request.POST,instance=UpdateData)
    if form.is_valid():
        form.save()
        messages.success(request, 'Plant ' + UpdateData.kigo+ ' is changed')
        return render(request, 'edit.html',{"Plants":UpdateData})

def DataDelete(request,id):
    DeleteData=Plants.objects.get(id=id)
    DeleteData.delete()
    showall=Plants.objects.all()
    return render(request, 'Index.html',{"data":showall})
