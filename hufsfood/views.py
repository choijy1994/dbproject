from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
from .forms import recommendForm
from .functions import restaurant as rstr


#테이블이름을 restaurant라고 가정

def index(request, show='default'):
    restaurants = Restaurant.objects.all()
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/init.html', context)

def show_chicken(request):
    restaurants = Restaurant.objects.filter(kind='치킨')
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/result.html', context)

def show_chinese(request):
    restaurants = Restaurant.objects.filter(kind='중국집')
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/result.html', context)

def show_pizza(request):
    restaurants = Restaurant.objects.filter(kind='피자/양식')
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/result.html', context)

def show_korean(request):
    restaurants = Restaurant.objects.filter(kind='한식')
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/result.html', context)

def show_cafe(request):
    restaurants = Restaurant.objects.filter(kind='카페/디저트')
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/result.html', context)

def show_snack(request):
    restaurants = Restaurant.objects.filter(kind='분식')
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/result.html', context)

def show_night(request):
    restaurants = Restaurant.objects.filter(kind='야식')
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/result.html', context)

def show_bossam(request):
    restaurants = Restaurant.objects.filter(kind='족발/보쌈')
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/result.html', context)

def show_japanese(request):
    restaurants = Restaurant.objects.filter(kind='일식/돈까스')
    context = {'restaurants':restaurants}
    return render(request, 'hufsfood/result.html', context)

def show_recommend(request):
    restaurant = rstr()

    if request.method == 'POST':
        form = recommendForm(request.POST or None)
        if form.is_valid():
            q = rstr.recommend(
                kind = form.cleaned_data.get('type_kind'),
                cost=form.cleaned_data.get('type_cost'),
                dist = form.cleaned_data.get('type_dist'),
                rate = form.cleaned_data.get('type_rate'),
                )

            restaurants = Restaurant.objects.filter(q)

            if not restaurants:
                context = {'msg': '일치하는 맛집이 없습니다.'}
            else:
                context = {'restaurants': restaurants}
        else:
            context = {'msg': '제출한 양식이 올바르지 않습니다.'}

        del restaurant
        return render(request, 'hufsfood/result.html', context)
    else:
        form = recommendForm(request.POST)


        del restaurant
        return render(request, 'hufsfood/recommend.html',{'form' : form})



