from django.urls import path
from . import views

urlpatterns = [
    # ex: /parkinglist/
    path('', views.index, name='index'),

    path('hufsfood/chicken',views.show_chicken,name = 'chicken'),
    path('hufsfood/chicken/',views.show_chicken,name = 'chicken'),

    path('hufsfood/chinese', views.show_chinese, name='chinese'),
    path('hufsfood/chinese/', views.show_chinese, name='chinese'),

    path('hufsfood/pizza', views.show_pizza, name='pizza'),
    path('hufsfood/pizza/', views.show_pizza, name='pizza'),

    path('hufsfood/korean', views.show_korean, name='korean'),
    path('hufsfood/korean/', views.show_korean, name='korean'),

    path('hufsfood/snack', views.show_snack, name='snack'),
    path('hufsfood/snack/', views.show_snack, name='snack'),

    path('hufsfood/cafe', views.show_cafe, name='cafe'),
    path('hufsfood/cafe/', views.show_cafe, name='cafe'),

    path('hufsfood/bossam', views.show_bossam, name='bossam'),
    path('hufsfood/bossam/', views.show_bossam, name='bossam'),

    path('hufsfood/night', views.show_night, name='night'),
    path('hufsfood/night/', views.show_night, name='night'),

    path('hufsfood/japanese', views.show_japanese, name='japanese'),
    path('hufsfood/japanese/', views.show_japanese, name='japanese'),

    path('hufsfood/recommend', views.show_recommend, name='recommend'),
    path('hufsfood/recommend/', views.show_recommend, name='recommend'),


    ]