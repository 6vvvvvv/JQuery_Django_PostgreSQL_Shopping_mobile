from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse  # ajax
from .models import Main, Nav, Mustbuy, Maingood, FoodType, Goods, User, Cart, Order
from django.urls import reverse  # redirect to other view
from .forms.login import LoginForm
from django.conf import settings  # upload img
from django.contrib.auth import logout

import os

import time  # generate token
import random  # generate token


# Create your views here.


def home(request):
    mainwheels = Main.objects.all()
    mainnavs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    maingoods = Maingood.objects.all()[0:4]
    maingoods1 = Maingood.objects.all()[4:]
    return render(request, 'home/home.html', {'mainwheels': mainwheels, 'mainnavs': mainnavs, 'mustbuys': mustbuys, 'maingoods': maingoods,'maingoods1':maingoods1})


def market(request):
    # redirect to marketparams to and pass arg
    return HttpResponseRedirect(reverse('axf:marketparams', args=('104749', '0', '0')))

# received arg from url cateid,cid,sortedid, should be identical


def marketparams(request, cateid, cid, sortedid):

    leftsidebar = FoodType.objects.all()
    productList = Goods.objects.filter(categoryid=cateid)

    # class filter
    if cid == 0:
        productList = Goods.objects.filter(categoryid=cateid)
    else:
        productList = Goods.objects.filter(categoryid=cateid, childcid=cid)

    # soldnum/price filter
    if sortedid == 0:
        pass
    elif sortedid == 1:
        productList = productList.order_by('soldnum')
    elif sortedid == 2:
        productList = productList.order_by('price')
    elif sortedid == 3:
        productList = productList.order_by('-price')

    # class filter algorithem :split by # then split by : and store in dictionary
    group = leftsidebar.get(typeid=cateid)
    # print(group.typeid)
    childList = []
    # type:0 # imported fruit:103534 # native fruit:103533 (data in FoodType)
    childnames = group.childtypenames
    childnamearr = childnames.split("#")
    for str in childnamearr:
        # type:0
        arr1 = str.split(":")

        # group.typeid will show the categoryid chosen in the leftsidebar or use cateid directly
        obj = {"childName": arr1[0],
               "childId": arr1[1], "parentId": group.typeid}
        childList.append(obj)

    # cart view and its operation
    # verify login or not
    # if login
    token = request.session.get("token")
    # print(token)
    carlist = []
    if token:
        user = User.objects.get(userToken=token)
        carlist = Cart.objects.filter(userAccount=user.userAccount)

    # add an attribute in p and show p.num otherwise default 0
    for p in productList:
        for c in carlist:
            if c.productid == p.productid:
                p.num = c.productnum

    # cateid cid sortedid should return important!!!!!!!!!!!!!!!!!!!

    return render(request, 'market/market.html', {'leftsidebar': leftsidebar, 'productList': productList,
                                                  'childList': childList, 'cateid': cateid, 'cid': cid, 'sortedid': sortedid})


def cart(request):
    token = request.session.get("token")
    # print(token)
    carlist = []
    if token:
        user = User.objects.get(userToken=token)
        carlist = Cart.objects.filter(userAccount=user.userAccount)

    return render(request, 'cart/cart.html', {"carlist": carlist, "user": user})


def changecart(request, flag):
    # verify if login
    token = request.session.get("token")
    if token == None:
        # return to js
        return JsonResponse({"data": -1, "status": "error"})

    # receive the productid from market.js post method and get the good from Goods
    productid = request.POST.get("productid")
    product = Goods.objects.get(productid=productid)

    # get current user via token
    user = User.objects.get(userToken=token)

    # order add
    if flag == 0:
        # verify the inventory
        if product.inventory == 0:
            return JsonResponse({"data": -2, "status": "error"})

        # get all the orders under userAccount  two case: exist or not
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = None

        if carts.count() == 0:

            # if not exist then create
            c = Cart.createcart(user.userAccount, productid, 1, product.price, True,
                                product.productimg, product.productname, False)
            c.save()
        else:
            try:
                # if exist
                # find the specific order and modify the num
                c = carts.get(productid=productid)
                c.productnum += 1
                # price CharField should convert to float and round 2 digits
                c.productprice = "%.2f" % (float(product.price)*c.productnum)
                c.save()

            except Cart.DoesNotExist as e:
                c = Cart.createcart(user.userAccount, productid, 1, product.price, True,
                                    product.productimg, product.productname, False)
                c.save()

        # goods invetory -1
        product.inventory -= 1
        product.save()

        return JsonResponse({"data": c.productnum, "price": c.productprice, "status": "success"})

    # order subtract
    if flag == 1:

        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = None

        if carts.count() == 0:
            return JsonResponse({"data": -2, "status": "error"})
        else:
            try:
                # if exist
                # find the specific order and modify the num
                c = carts.get(productid=productid)
                c.productnum -= 1
                c.productprice = "%.2f" % (float(product.price)*c.productnum)

                # if product num in order equals 0 then delete
                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()

            except Cart.DoesNotExist as e:
                return JsonResponse({"data": -2, "status": "error"})

        # goods invetory -1
        product.inventory += 1
        product.save()

        return JsonResponse({"data": c.productnum, "price": c.productprice, "status": "success"})

    if flag == 2:

        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = carts.get(productid=productid)
        c.isChose = not c.isChose
        c.save()

        str = ""
        if c.isChose:
            str = "√"

        return JsonResponse({"data": str, "status": "success"})


def mine(request):
    token = request.session.get("token")

    if token != None:
        user = User.objects.get(userToken=token)
        return render(request, 'mine/mine.html', {"user": user})
    else:
        return redirect('/axf/login/')


def login(request):
    if request.method == 'POST':
        f1 = LoginForm(request.POST)
        if f1.is_valid():
            # print('**********************************************')
            nameid = f1.cleaned_data['username']
            pswd = f1.cleaned_data['passwd']

            try:
                user = User.objects.get(userAccount=nameid)

                if user.userPasswd != pswd:

                    return redirect('/axf/login/')

            except User.DoesNotExist as e:

                return redirect('/axf/login/')

            # helloUser = user.userAccount

            # if verification success

            # generate randomly
            userToken = time.time()+random.randrange(1, 100000)
            userToken = str(userToken)
            user.userToken = userToken
            user.save()

            request.session["username"] = user.userName
            request.session["token"] = user.userToken
            # "/" prefix important
            # print("************************444444444444444444444")
            return render(request, 'mine/mine.html', {"user": user})
        else:
            return render(request, 'user/user_login.html', {"title": "login", "form": f1, "error": f1.errors})
    else:
        # if requeste method is GET
        f1 = LoginForm()
        return render(request, 'user/user_login.html', {"title": "login", "form": f1})


def register(request):
    if request.method == 'POST':
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPasswd")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAddr = request.POST.get("userAddr")
        userIcon = request.POST.get("userIcon")

        # generate randomly
        userToken = time.time()+random.randrange(1, 100000)
        userToken = str(userToken)

        # upload img
        f = request.FILES.get("useIcon")
        userIcon = os.path.join(settings.MEDIA_ROOT, userAccount+".jpg")
        with open(userIcon, "wb") as fp:
            for data in f.chunks():
                fp.write(data)

        # write into postgresql
        newUser = User.objects.create(userAccount=userAccount, userPasswd=userPasswd,
                                      userName=userName, userPhone=userPhone, userAddress=userAddr, userIcon=userIcon, userToken=userToken)
        newUser.save()

        # save to session
        request.session["username"] = userName
        request.session["token"] = userToken

        return redirect('/axf/mine/')
    else:
        pass

    # if requeste method is GET
        return render(request, 'user/user_register.html', {})


def check(request):
    # "userid" is the second parameter of post method in js
    userid = request.POST.get("userid")
    try:
        user = User.objects.get(userAccount=userid)
        # "user exist", "error" will respectively pass to (data) in js
        return JsonResponse({"data": "user exist", "status": "error"})

    except User.DoesNotExist as e:
        return JsonResponse({"data": "ok", "status": "success"})


def quit(request):
    logout(request)
    return redirect('/axf/login/')


def saveorder(request):
    token = request.session.get("token")

    if token == None:
        # return to js
        return JsonResponse({"data": -1, "status": "error"})

    user = User.objects.get(userToken=token)
    cart = Cart.objects.filter(isChose=True)

    if cart.count() == 0:
        return JsonResponse({"data": -1, "status": "error"})

    orderid = time.time()+random.randrange(1, 100000)
    orderid = str(orderid)

    o = Order.createorder(orderid, user.userAccount, 0)
    o.save()

    # save to model cart isDlete and orderid is empty by defaut
    for item in cart:
        item.isDelete = True
        item.orderid = orderid
        item.save()

    return JsonResponse({"status": "success"})
