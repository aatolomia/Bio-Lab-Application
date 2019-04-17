from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Sum
from datetime import date
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Item, Category, Borrow

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

        item = Item(name=name, available=available)
        item.save()
        if item.categories.add(cat):
            return redirect('/items')
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, "items/items.html", {"items": items, "categories": categories})


def delete_category(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    return redirect('/categories')

def delete_item(request, id):
    item = Item.objects.filter(id=id).get()
    item.delete()
    return redirect("/items")

def borrow(request):
    if request.method == "POST":
        #student_id = request.POST['student_id']
        #student = Student.objects.get(id=student_id)
        status = "Borrowed"
        items_id = request.POST.getlist('selector')
        for item_id in items_id:
            item = Item.objects.get(id=item_id)
            i = Borrow(qty=1, status=status)
            i.save()
          #  i.student.add(student)
            i.item.add(item)
            return redirect("/borrow")
  #  students = Student.objects.all()
    items = Item.objects.all()
    datas = []
    for item in items:
        left = Borrow.objects.filter(status="Borrowed", item__name=item.name).aggregate(Sum('qty'))
        if left['qty__sum'] is None:
            l = 0
        else:
            l = int(left['qty__sum'])
        datas.append(item.available - l)
    return render(request, "items/borrow.html", {"datas": zip(items, datas)})


def approvereturn(request):
    if request.method == "POST":
        i_id = int(request.POST["borrow_id"])
        borrow = Borrow.objects.get(id=i_id)
        borrow.date = datetime.now()
        borrow.status = "Returned"
        borrow.save()
        return redirect('/approvereturn')
    borrows = Borrow.objects.all()
    return render(request, "items/return.html", {"borrows": borrows})
