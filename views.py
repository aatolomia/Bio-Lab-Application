from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum
from datetime import date
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Item, Category, Borrow, Pending

def categories(request):
    if request.method == "POST":
        name = request.POST['name']
        Category(name=name).save()
        return redirect('/categories')
    categories = Category.objects.all()
    return render(request, "items/category.html", {"categories": categories})

def edit_category(request, id):
    category = Category.objects.filter(id=id).get()
    return JsonResponse({'name': category.name})

def edit_item(request, id):
    item = Item.objects.filter(id=id).get()
    return JsonResponse(
        {'name': item.name, 'available': item.available})

def items(request):
    if request.method == "POST":
        name = request.POST['name']
        cat = Category.objects.get(id=int(request.POST['category_id']))
        available = int(request.POST['quantity'])
        picture = request.FILES['picture']
        
        item = Item(name=name, available=available, picture=picture)
        item.save()
        if item.categories.add(cat):
            return redirect('/items')
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, "items/items.html", {"items": items, "categories": categories})

def request(request):
    pend = Pending.objects.all()
    if request.method == "POST":
        
        items_id = request.POST.get('select')
        if items_id:

            pend = Pending.objects.get(pk=items_id)
            borrow = Borrow()
            borrow.borrower = pend.user_borrow
            borrow.name_item = pend.name_of_item
            borrow.num_of_items = pend.num_of_items
            borrow.picture = pend.picture
            borrow.date = datetime.now()
            borrow.save()
            pend.delete()
            return redirect('/request')
        else:
            return redirect('/request')

    return render(request, "items/request.html", {"pend": pend})

def delete_category(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    return redirect('/categories')

def delete_item(request, id):
    item = Item.objects.filter(id=id).get()
    item.delete()
    return redirect("/items")




def borrow(request):
    items = Item.objects.all()
    if request.method == "POST":
        
        status = "Borrowed"
        items_id = request.POST.get('selector')
        
        
        num = request.POST.get('num')
        if num and items_id:
            num = int(request.POST.get('num'))
            pend = get_object_or_404(Item, pk=items_id)
            it = get_object_or_404(Item, pk=items_id)
            pending = Pending()
            pending.user_borrow = request.user
            pending.name_of_item = pend.name
            pending.num_of_items = request.POST.get('num')
            #pending.num_borrowed = pend.available-1
            pending.picture = pend.picture
            it.available = pend.available-num
            if it.available < 0:
                messages.error(request,'Invalid')
                return redirect("/borrow")
            #instance = cart.save(commit=False)
            #instance.user_b = request.user
            else:
                it.save()
                pending.save()
                return redirect("/borrow")
        else:
            return redirect("/borrow")
       
  #  students = Student.objects.all()
    
    return render(request, "items/borrow.html", {'items':items})


def approvereturn(request):
    borrows = Borrow.objects.all()
    return render(request, "items/return.html", {"borrows": borrows})
