from django.urls import path, include
from .models import Category , Product , CaseFanFeature, CoolerFeature,  MotherboardFeature , ComputerCaseFeature , GraphicsCardFeature ,ProcessorFeature , KeyboardFeature , MonitorFeature,MouseFeature , RamFeature
from rest_framework import  serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","name","description","image_url")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id","name","price","image_url","category")


class MotherBoardFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherboardFeature
        fields = ("id","processor_Socket_Type" , "ram_Type" , "compatible_Processors",  "motherboard_Size"  , "product")
        

class ComputerCaseFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ComputerCaseFeature
        fields =  ("id","case_Type", "PSU" ,  "PSU_Location" , "transparent_Case" ,  "type_C" , "product")

class GraphicsCardFeatureSerializer(serializers.ModelSerializer) : 
    class Meta :
        model = GraphicsCardFeature
        fields =  ("id","gpu_Manufacturer" , "gpu_Model" , "memory_Type" , "gpu_Memory_Capacity" , "product" )


class  ProcessorFeatureSerializer(serializers.ModelSerializer) :
    class Meta:
        model =  ProcessorFeature
        fields =  ("id" ,"processor_Model" , "processor_Manufacturer" , "processor_Socket_Type" , "processor_Series" , "core_Count","product")



class CaseFanFeatureSerializer(serializers.ModelSerializer):
    class Meta :
        model =  CaseFanFeature
        fields =  ("id","cooling_Type" , "fan_Count" , "led_Type" , "power_Connector" , "rpm","product")
        
class KeyboardFeatureSerializer(serializers.ModelSerializer):
      class Meta :
        model =  KeyboardFeature
        fields =  ("id","connection_Type" , "mechanical" , "keyboard_Layout" , "wrist_Support" , "numpad","product")


class MonitorFeatureSerializer(serializers.ModelSerializer):
      class Meta :
        model =  MonitorFeature
        fields =  ("id","screen_Size" , "resolution" , "refresh_Rate" , "panel_Type" , "response_Time","product")
    

class MouseFeatureSerializer(serializers.ModelSerializer):
      class Meta :
        model =  MouseFeature
        fields =  ("id","connection_Type" , "tracking_Type" , "button_Count" , "usage_Type" , "max_DPI" , "product")
    
class RamFeatureSerializer(serializers.ModelSerializer):
      class Meta :
        model =  RamFeature
        fields =  ("id","ram_Type" , "ram_Capacity" , "ram_Frequency" , "channel_Type" , "ram_Compatibility" , "product")

class CoolerFeatureSerializer(serializers.ModelSerializer):
      class Meta :
        model =  CoolerFeature
        fields =  ("id","compatible_Sockets" , "cooling_Type" , "led" , "radiator_Size" , "fan_Count" , "product")