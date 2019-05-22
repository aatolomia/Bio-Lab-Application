from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum
from datetime import date
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Item, Category, Borrow, Pending

def categories(request):#add category (admin)                                                                                                        
    if request.method == "POST":
        name = request.POST['name']
        picture = request.FILES['picture']
        Category(name=name,picture=picture).save()
        return redirect('/ChemAid/categories')
    categories = Category.objects.all()
    return render(request, "items/category.html", {"categories": categories})

def edit_category(request, id): #edit category (admin)
    category = Category.objects.filter(id=id).get()
    return JsonResponse({'name': category.name})

def edit_item(request, id): #edit item (admin)
    item = Item.objects.filter(id=id).get()
    return JsonResponse(
        {'name': item.name, 'available': item.available})

def items(request): #add item (admin)
    if request.method == "POST":
        name = request.POST['name']
        cat = Category.objects.get(id=int(request.POST['category_id']))
        available = int(request.POST['quantity'])
        picture = request.FILES['picture']
        
        item = Item(name=name, available=available, picture=picture)
        item.save()
        if item.categories.add(cat):
            return redirect('/ChemAid/items')
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, "items/items.html", {"items": items, "categories": categories})

def request(request): #approving of the borrowed items
    pend = Pending.objects.all()
    if request.method == "POST":
        
        items_id = request.POST.get('select')
        num = request.POST.get('num')
        if num and items_id:
            
            pend = get_object_or_404(Pending, pk=items_id)
            #it = Item.objects.get(pk=items_id)
            borrow = Borrow()
            borrow.borrower = pend.user_borrow
            borrow.name_item = pend.name_of_item
            borrow.cat_name = pend.cat_name
            borrow.picture = pend.picture
            borrow.date = datetime.now()
            
            #it.available = it.available+pend.num_of_items
            try:
                num = int(request.POST.get('num'))
                borrow.num_of_items = request.POST.get('num')
                pend.num_of_items = pend.num_of_items-num
                if pend.num_of_items < 0:
                    messages.error(request, 'Invalid')
                    return redirect('/ChemAid/request')
                if num < 0:
                    messages.error(request, 'Invalid')
                    return redirect('/ChemAid/request')
                else:
                    #it.save()
                    borrow.save()
                    pend.delete()
                    return redirect('/ChemAid/request')
            except ValueError:
                messages.error(request, 'Invalid')
                return redirect('/ChemAid/request')
        else:
            return redirect('/ChemAid/request')

    return render(request, "items/request.html", {"pend": pend})

def delete_category(request, id): 
    category = Category.objects.filter(id=id)
    category.delete()
    return redirect('ChemAid/categories')

def delete_item(request, id):
    item = Item.objects.filter(id=id).get()
    item.delete()
    return redirect("ChemAid/items")

def borrow(request, id):
    items = Item.objects.all()
    cat = get_object_or_404(Category, pk=id)
    if request.method == "POST":
        
        status = "Borrowed"
        items_id = request.POST.get('selector')
        
        num = request.POST.get('num')
        if num and items_id:
            
            pend = get_object_or_404(Item, pk=items_id)
            it = get_object_or_404(Item, pk=items_id)
            pending = Pending()
            pending.user_borrow = request.user
            pending.name_of_item = pend.name
            pending.picture = pend.picture
            try:
                num = int(request.POST.get('num'))
                pending.num_of_items = request.POST.get('num')
                it.available = pend.available-num
                if it.available < 0:
                    messages.error(request,'Invalid')
                    return redirect("/ChemAid/borrow/" +id)
                if num < 0:
                    messages.error(request,'Invalid')
                    return redirect("/ChemAid/borrow/" +id)
                else:
                    it.save()
                    pending.save()
                    return redirect("/ChemAid/borrow/" +id)
            except ValueError:
                messages.error(request,'Invalid')
                return redirect("/ChemAid/borrow/" +id)
            
        else:
            return redirect("/ChemAid/borrow/" +id)
       
  #  students = Student.objects.all()
    
    return render(request, "items/borrow.html", {'items':items, 'cat':cat})

def cart(request):
    user_b = request.user
    return render(request,"items/cart.html", {'user_b':user_b})

def approvereturn(request):#(admin)list of approved borrowed items
    borrows = Borrow.objects.all()
    return render(request, "items/return.html", {"borrows": borrows})


def options(request):
    category = Category.objects.all()
    return render(request,"items/categ.html",{'category':category})

def cancel(request, id):
    pend = Pending.objects.all()
    pends = Pending.objects.filter(id=id).get()
    items = Item.objects.get(name=pends.name_of_item)
    items.available = items.available+pends.num_of_items
    user = pends.user_borrow.email
    #print(user)
    send_mail(
        'Request for items',
        'Your request was not approved.',
        'biochemaid.com',
        [user],
        fail_silently=False,
    )
    items.save()
    pends.delete()

    return render(request, "items/request.html", {"pend": pend, "items": items, "pends": pends})