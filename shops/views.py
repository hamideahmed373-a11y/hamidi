from django.shortcuts import render,HttpResponse

from .models import *
from .forms import *
from.urls import *
from django.db.models import Q

def product_details(request,productid):
    ps=Offers.objects.get(id=int(productid))
    return render(request, 'detail.html', {'product':ps})

def shop_details(request,shopid):
    product_of_shop=Offers.objects.filter(shop_id=int(shopid))
    shop_we_need=Base.objects.get(id=int(shopid))
    return render(request, 'final.html', {'shop':shop_we_need,'products':product_of_shop})

def base(request):
    form=BaseForm()
    if request.method=='POST':
        form=BaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    contex={'forms':form}
    return render(request,'new.html', contex)

def product_page(request):
    form=OffersForm()
    if request.method=='POST':
        form=OffersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    contex={'forms':form}
    return render(request,'new.html', contex)



def all_product(request):
    all_products = Offers.objects.all()
    if request.method == 'POST':
        searched = request.POST['searched']
        all_products = Offers.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) | Q(category__icontains=searched))

        return render(request, 'hello5.html', {'products': all_products})
        # Create your views here.
    else:
        return render(request, 'hello5.html', {'products': all_products})




def all_shop(request):
    all_shops=Base.objects.all()
    if request.method == 'POST':
        searched = request.POST['searched']
        all_shops = Base.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) | Q(shop_type__icontains=searched))

        return render(request, 'hello5.html', {'shops': all_shops})
        # Create your views here.
    else:
        return render(request, 'hello5.html', { 'shops': all_shops})



def home(request):
    shops=Base.objects.all()
    products=Offers.objects.all()


    if request.method == 'POST':
        searched = request.POST['searched']
        products = Offers.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) | Q(category__icontains=searched))
        shops = Base.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched) | Q(shop_type__icontains=searched))

        return render(request, 'hello5.html', {'products': products, 'shops': shops})
        # Create your views here.
    else:
        return render(request, 'hello5.html', {'products': products, 'shops': shops})

# Create your views here.
def how(request):
    video=How.objects.all()
    return render(request,'dashboard.html',{'videos':video})
def ads_txt_view(request):
    # Option 1: Inline content (simplest)
    content = 'google.com, ca-pub-1111613373641129T, f08c47fec0942fa0\n'
    return HttpResponse(content, content_type='text/plain')

