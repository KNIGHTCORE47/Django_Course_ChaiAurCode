from django.shortcuts import render, get_object_or_404
from .models import Different_Chais

# Create your views here.
def home(request):
    return render(request, 'chai_store/home.html')

def products(request):
    all_chais = Different_Chais.objects.all()

    return render(request, 'chai_store/products.html', {'items': all_chais})


def product_description(request, params):
    # pk = primary key
    product_id = get_object_or_404(Different_Chais, pk=params)

    return render(request, 'chai_store/description.html', {'product': product_id})