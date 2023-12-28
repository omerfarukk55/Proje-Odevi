from django.urls import path
from . import views

app_name = 'parts_of_computer_app'


urlpatterns = [

    # api urls
    path('category/' , views.category),
    path("product/" , views.product),
    path("category_details/<id>" , views.category_details),
    path('product_details/<id>' , views.product_details),
   
    path('motherboard/<product>' , views.motherboard),
    path("computer_case/<product>" , views.computer_case),
    path('graphics_card/<product>' , views.graphics_card),
    path('processor/<product>' , views.processor),
    path('case_fan/<product>' , views.case_fan),
    path('keyboard/<product>' , views.keyboard),
    path('monitor/<product>' , views.monitor),
    path('mouse/<product>' , views.mouse),
    path('ram/<product>' , views.ram),    
    path('cooler/<product>' , views.cooler),

]
