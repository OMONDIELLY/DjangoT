from django.http import Http404
from django.shortcuts import render, get_object_or_404,redirect
from .models import product
from .forms import ProductForm ,RawProductForm
# Create your views here.




def product_create_view(request):
    
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST or None)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            product.objects.create(**my_form.cleaned_data)
           
    
 
    context = {
        'form':my_form
    }
    return render(request, "products/product_create.html",context)

def dynamic_lookup_view(request, my_id):
    # obj = product.objects.get(id=my_id )
    obj = get_object_or_404(product,id=my_id) 
    obj = product.objects.get(id=my_id )
    try:
        obj = product.objects.get(id=my_id )
    except product.DoesNotExist:
        raise Http404

    context = {
        'object':obj
    }
    return render(request, "products/product_details.html",context)
    
def product_view_detail(request, id):
    obj = product.objects.get(id)
    context = {
        'object':obj
    }
    return render(request, "products/product_details.html",context)
   
def product_delete_view(request,my_id):
    obj = get_object_or_404(product,id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        'object':obj
    }
    return render(request, "products/product_delete.html",context)

def product_list_view(request):
    queryset = product.objects.all()
    context = {
        'object_list': queryset
        
    }
    return render(request, "products/product_list.html",context)