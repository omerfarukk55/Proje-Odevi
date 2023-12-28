from django.shortcuts import render
from . import models
from .models import Category , Product , MotherboardFeature ,ComputerCaseFeature ,GraphicsCardFeature ,ProcessorFeature ,CaseFanFeature ,KeyboardFeature ,MonitorFeature , MouseFeature ,RamFeature ,CoolerFeature
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer , ProductSerializer , KeyboardFeatureSerializer, CoolerFeatureSerializer , RamFeatureSerializer , MonitorFeatureSerializer ,MotherBoardFeatureSerializer , CaseFanFeatureSerializer , MouseFeatureSerializer , ComputerCaseFeatureSerializer , GraphicsCardFeatureSerializer ,ProcessorFeatureSerializer


# Create your views here.

def anakart_view(request):
    anakart = models.Product.objects.filter(category_id = 2)
    anakart_dict={"anakartlar":anakart}
    return render(request, 'parts_of_computer_app/anakart.html', context=anakart_dict)


def bilgisayar_kasalari_view(request):  
    bilgisayar_kasalari = models.Product.objects.filter(category_id = 5)
    bilgisayar_kasalari_dict={"bilgisayar_kasalari": bilgisayar_kasalari}   
    return render(request, 'parts_of_computer_app/bilgisayar-kasalari.html',context=bilgisayar_kasalari_dict)

def ekran_karti_view(request):
    ekran_karti = models.Product.objects.filter(category_id = 4)
    ekran_karti_dict={"ekran_kartlari": ekran_karti}       
    return render(request, 'parts_of_computer_app/ekran-karti.html',context=ekran_karti_dict)

def islemci_view(request):
    islemci = models.Product.objects.filter(category_id = 1)
    islemci_dict={"islemciler": islemci}
    return render(request, 'parts_of_computer_app/islemci.html', context= islemci_dict)

def ram_view(request):
    ram = models.Product.objects.filter(category_id = 3)
    ram_dict={"rams": ram}    
    return render(request, 'parts_of_computer_app/ram.html', context= ram_dict)

def islemci_sogutucular_view(request):
    sogutucu = models.Product.objects.filter(category_id = 6)
    sogutucu_dict={"sogutucular": sogutucu}    
    return render(request, 'parts_of_computer_app/sogutucular.html', context= sogutucu_dict)

def kasa_fanlari_view(request):
    kasa_fanlari = models.Product.objects.filter(category_id = 7)
    kasa_fanlari_dict={"kasa_fanlari": kasa_fanlari}    
    return render(request, 'parts_of_computer_app/kasa-fanlari.html', context= kasa_fanlari_dict)

def termal_macun_view(request):
    termal_macun = models.Product.objects.filter(category_id = 8)
    termal_macun_dict={"termal_macunlar": termal_macun}    
    return render(request, 'parts_of_computer_app/termal-macun.html', context= termal_macun_dict)

def klavye_view(request):
    klavyeler = models.Product.objects.filter(category_id = 9)
    klavyeler_dict={"klavyeler": klavyeler}    
    return render(request, 'parts_of_computer_app/klavye.html', context= klavyeler_dict)

def monitor_view(request):
    monitorler = models.Product.objects.filter(category_id = 10)
    monitorler_dict={"monitorler": monitorler}    
    return render(request, 'parts_of_computer_app/monitor.html', context= monitorler_dict)

def mouse_view(request):
    mouse = models.Product.objects.filter(category_id = 11)
    mouse_dict={"mouseler": mouse}    
    return render(request, 'parts_of_computer_app/mouse.html', context= mouse_dict)

def home_view(request):
    
    products = models.Product.objects.all()
    products_dict = {"products": products}
    return render(request, 'parts_of_computer_app/home.html',context=products_dict)




# -----------------------------------------------



@api_view(['GET'])
def category(request):
    if request.method == 'GET':
        data = Category.objects.all()
        serializer = CategorySerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def product(request):
    if request.method == "GET":
        data = Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return  Response(serializer.data)


@api_view(["GET"])
def product_details(request , id):
    if request.method == "GET":
        data = Product.objects.filter(id = id )
        serializer = ProductSerializer(data, many=True)
        return  Response(serializer.data)



@api_view(["GET"])
def category_details(request, id):
    if request.method == "GET":
        data = Product.objects.filter(category = id)
        serializer = ProductSerializer(data, many=True)
        return  Response(serializer.data)



@api_view(["GET"])
def motherboard(request , product):
    if request.method == 'GET':
        data = MotherboardFeature.objects.filter(product = product)
        serializer = MotherBoardFeatureSerializer(data, many=True)
        return  Response(serializer.data)
    
    
@api_view(["GET"])
def computer_case(request ,product):
    if request.method == 'GET':
        data = ComputerCaseFeature.objects.filter(product = product)
        serializer = ComputerCaseFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def  graphics_card(request,product):
    if request.method == 'GET':
        data = GraphicsCardFeature.objects.filter(product = product)
        serializer = GraphicsCardFeatureSerializer(data, many=True)
        return  Response(serializer.data)
@api_view(["GET"])  
def  processor(request,product):
    if request.method == 'GET':
        data = ProcessorFeature.objects.filter(product = product)
        serializer = ProcessorFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def case_fan(request,product):
    if request.method == 'GET':
        data = CaseFanFeature.objects.filter(product = product)
        serializer = CaseFanFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def keyboard(request,product):
    if request.method == 'GET':
        data = KeyboardFeature.objects.filter(product = product)
        serializer = KeyboardFeatureSerializer(data, many=True)
        return  Response(serializer.data)
@api_view(["GET"])
def monitor(request,product):
    if request.method == 'GET':
        data = MonitorFeature.objects.filter(product = product)
        serializer = MonitorFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def mouse(request,product):
    if request.method == 'GET':
        data = MouseFeature.objects.filter(product = product)
        serializer = MouseFeatureSerializer(data, many=True)
        return  Response(serializer.data)
@api_view(["GET"])
def ram(request,product):
    if request.method == 'GET':
        data = RamFeature.objects.filter(product = product)
        serializer = RamFeatureSerializer(data, many=True)
        return  Response(serializer.data)

@api_view(["GET"])
def cooler(request,product):
    if request.method == 'GET':
        data = CoolerFeature.objects.filter(product = product)
        serializer = CoolerFeatureSerializer(data, many=True)
        return  Response(serializer.data)
