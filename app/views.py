from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from.models import Order, Inventory

class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log the user in after signup
        return redirect('login') 


class ShopPageView(TemplateView):
    template_name= 'app/shop.html'


class AboutPageView(TemplateView):
    template_name= 'app/about.html'


class LearMoreView(TemplateView):
    template_name= 'app/learnmore.html'


class LoginView(TemplateView):
    template_name= 'app/login.html'

class RegisterView(TemplateView):
    template_name= 'app/signup.html'

class ProcessView(TemplateView):
    template_name= 'app/process.html'


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



from.models import Order, Category, Customer, Product, Inventory


class HomePageView(TemplateView):
    template_name = 'app/home.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'





class OrderListView(ListView):
    model = Order
    context_object_name = 'order'
    template_name = 'app/order_list.html'

class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'app/order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    fields = ['customer', 'product', 'total_amount']
    template_name = 'app/order_create.html'
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['customer', 'product', 'total_amount']
    template_name = 'app/order_update.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'app/order_delete.html'
    success_url = reverse_lazy('order_list')






class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'app/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'app/category_detail.html'


class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'app/category_create.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'app/category_update.html'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'app/category_delete.html'
    success_url = reverse_lazy('category_list')




class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'app/customer_list.html'


class CustomerDetailView(DetailView):
    model = Customer
    context_object_name = 'customer'
    template_name = 'app/customer_detail.html'


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name = 'app/customer_create.html'
    success_url = reverse_lazy('customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name = 'app/customer_update.html'
    success_url = reverse_lazy('customer_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'app/customer_delete.html'
    success_url = reverse_lazy('customer_list')




class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'app/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'app/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'description', 'quantity', 'Category']
    template_name = 'app/product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'description', 'quantity', 'Category']
    template_name = 'app/product_update.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'app/product_delete.html'
    success_url = reverse_lazy('product_list')




class InventoryListView(ListView):
    model = Inventory
    template_name = 'app/inventory_list.html'
    context_object_name = 'inventories'

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'app/inventory_detail.html'
    context_object_name = 'inventory'


class InventoryCreateView(CreateView):
    model = Inventory
    fields = ['product', 'quantity']  # Only product and quantity fields (other fields are auto-filled)
    template_name = 'app/inventory_create.html'
    success_url = reverse_lazy('inventory_list')    

class InventoryUpdateView(UpdateView):
    model = Inventory
    fields = ['product', 'quantity']
    template_name = 'app/inventory_update.html'
    success_url = reverse_lazy('inventory_list')

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'app/inventory_delete.html'
    success_url = reverse_lazy('inventory_list')