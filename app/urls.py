from django.contrib.admin.templatetags.admin_list import pagination_tag
from django.urls import path
from django.shortcuts import redirect
from .views import RegisterView
from .views import ShopPageView, AboutPageView, LoginView, RegisterView, OrderCreateView, ProcessView
from .views import(
    OrderListView,
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    CustomerListView,
    CustomerDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductListView,
    ProductDetailView,
    InventoryListView,
    InventoryUpdateView,
    InventoryDeleteView,
    InventoryCreateView,
    InventoryDetailView,
    
    
  
    
   
)


urlpatterns = [

    path('', lambda request: redirect('login')),
    path('register/',RegisterView.as_view(), name= 'signup' ),
    path('shop/',ShopPageView.as_view(), name= 'shop'),
    path('about/', AboutPageView.as_view(), name= 'about'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('', OrderCreateView.as_view(), name='order_create'),
    path('process/', ProcessView.as_view(), name='process'),




    path('order/', OrderListView.as_view(), name='order'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('order/', OrderListView.as_view(), name='order_list'),




    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    


    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),




    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),





    path('inventory/', InventoryListView.as_view(), name='inventory_list'),  # List all inventory items
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory_detail'),  # View details of an individual inventory item
    path('inventory/create/', InventoryCreateView.as_view(), name='inventory_create'),  # Create a new inventory item
    path('inventory/update/<int:pk>/', InventoryUpdateView.as_view(), name='inventory_update'),  # Update an existing inventory item
    path('inventory/delete/<int:pk>/', InventoryDeleteView.as_view(), name='inventory_delete'),  # Delete an inventory item



]






