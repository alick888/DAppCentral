from django.shortcuts import render

# Create your views here.
def sotadmin(request):
    return render(request, 'sotadmin/index.html')

def wallet(request):
    return render(request, 'sotadmin/wallet.html')

def iotcat(request):
    return render(request, 'sotadmin/iot-cat.html')

def iotcatdetail(request):
    return render(request, 'sotadmin/iot-cat-detail.html')

def iotmoddetail(request):
    return render(request, 'sotadmin/iot-mod-detail.html')

def iotversion(request):
    return render(request, 'sotadmin/iot-version.html')

def iotversiondetail(request):
    return render(request, 'sotadmin/iot-version-detail.html')
