from django.urls import path, include, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('market/', views.market, name='market'),
    path('market/<int:cateid>/<int:cid>/<int:sortedid>/',
         views.marketparams, name='marketparams'),
    path('cart/', views.cart, name='cart'),
    # path('mine/', views.mine, name='mine'),
    re_path(r'^mine/$', views.mine, name='mine'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/checkuser/', views.check, name='checkid'),
    path('quit/', views.quit, name='quit'),
    path('changecart/<int:flag>/', views.changecart, name='changecart'),
    path('saveorder/', views.saveorder, name='saveorder')
]
