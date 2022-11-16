from django.shortcuts import render

# Create your views here.

# This is Ecommerece webs app created by wasim-chadhar
from django.http import HttpResponse
from .models import Product, Contact, Order, Order_track
from math import ceil

def index(request):
    items = Product.objects.all()
    
    # allItems = [[items, range(1, len(items)),nSlide], [items, range(1, len(items)),nSlide] ]
    allItems = []
    product_category = Product.objects.values('product_catageory', 'id')
    categorys = {item['product_catageory'] for item in product_category}
    for prod_category in categorys:
        product = Product.objects.filter(product_catageory = prod_category)
        total_items = len(items)
        nSlide = total_items // 4 + ceil((total_items/4) - (total_items//4))
        allItems.append([product, range(1, nSlide), nSlide])
    params = {
        'allItems': allItems

    }

    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')

        contact= Contact(name=name, email=email, query_desc=desc)
        contact.save()

    return render(request, 'shop/contact.html')


def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    item = Product.objects.filter(id=myid)

    return render(request, 'shop/productView.html', {'item': item[0]})


def tracker(request):
    if request.method == "POST":
        orderId= request.POST.get('orderId', '')
        email = request.POST.get('email', '')

        # print(orderId, email)

        try:
            order = Order.objects.filter(order_id = orderId, buyer_email=email)
            # print("order : ", order)
            if len(order) > 0:
                update = Order_track.objects.filter(order_id = orderId)
                print("update::" ,update)
                updates = []

                for item in update:
                    print(item)
                    updates.append({'text':item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates,order[0].buyer_items_json, default=str)
                # print(response)
                return HttpResponse(response)

            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def checkout(request):
    if request.method == "POST":
        itemsJson = request.POST.get('itemsJson', '')
        name = request.POST.get('fname', '') + " " + request.POST.get('lname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        adress = request.POST.get('adress1', '') + " " + request.POST.get('adress2', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        zipCode = request.POST.get('zipCode', '')

        order= Order(buyer_items_json=itemsJson, buyer_name=name, buyer_email=email, buyer_phone=phone, 
        buyer_adress=adress, buyer_state=state, buyer_city=city, buyer_zipCode=zipCode)
        order.save()

        update= Order_track(order_id= order.order_id, update_desc="The order has been placed")
        update.save()

        thanks=True
        id= order.order_id

        return render(request, 'shop/checkout.html', {'thanks':thanks, 'id':id})
    return render(request, 'shop/checkout.html')


