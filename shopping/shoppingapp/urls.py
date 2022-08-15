from django.urls import path
from . import views

app_name = 'shopping'

urlpatterns = [

    path('', views.alProdCat, name='alProdCat'),
    path('<slug:c_slug>/', views.alProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productdetail, name='productdetail'),

]
