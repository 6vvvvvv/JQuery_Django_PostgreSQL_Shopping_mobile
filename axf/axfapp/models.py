from django.db import models


# Create your models here.

class Main(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Nav(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['trackid']


class Mustbuy(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Maingood(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class FoodType(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=200)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    def __str__(self):
        return self.typename

    class Meta:
        ordering = ['typesort']


class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    onefree = models.CharField(max_length=200)
    specifics = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    originprice = models.FloatField(default=1)
    categoryid = models.CharField(max_length=20)
    childcid = models.CharField(max_length=20)
    childcidname = models.CharField(max_length=200)
    detailid = models.CharField(max_length=20)
    inventory = models.IntegerField(default=1)
    soldnum = models.IntegerField(default=1)

    def __str__(self):
        return self.productname

# by default filter isdelete=false item from the list when apply objects
class CartManager(models.Manager):
    def get_queryset(self):
        return super(CartManager, self).get_queryset().filter(isDelete=False)


class Cart(models.Model):
    userAccount = models.CharField(max_length=20)
    productid = models.CharField(max_length=20)
    productnum = models.IntegerField()
    productprice = models.CharField(max_length=20)
    isChose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    orderid = models.CharField(max_length=20, default="0")
    isDelete = models.BooleanField(default=False)
    objects = CartManager() #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # object2 = CartManage2()

    def __str__(self):
        return self.orderid

    @classmethod
    def createcart(cls, userAccount, productid, productnum, productprice, isChose,
                   productimg, productname, isDelete):

        c = cls(userAccount=userAccount, productid=productid, productnum=productnum,
                productprice=productprice, isChose=isChose, productimg=productimg,
                productname=productname, isDelete=isDelete)

        return c


# it can define in forms as well,just same as loginform
class User(models.Model):

    userAccount = models.CharField(max_length=20, unique=True)
    userPasswd = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    userPhone = models.CharField(max_length=20)
    userAddress = models.CharField(max_length=200)
    userIcon = models.CharField(max_length=200)
    userToken = models.CharField(max_length=200, default="")
    userRank = models.IntegerField(default=0)

    @classmethod
    def createuser(cls, account, passwd, name, phone, address, icon, token, rank):
        newuser = cls(userAccount=account, userPasswd=passwd, userName=name, userPhone=phone,
                      userAddress=address, userIcon=icon, userToken=token, userRank=rank)

        return newuser

        


class Order(models.Model):
    orderid = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)
    progress = models.IntegerField()

    @classmethod
    def createorder(cls, orderid, userid, progress):
        o = cls(orderid=orderid, userid=userid, progress=progress)
        return o
