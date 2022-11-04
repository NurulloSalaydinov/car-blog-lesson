from django.shortcuts import render, redirect
from .models import Brand, Car, Comment
from .forms import CommentForm


def home(request):
    brands = Brand.objects.all().order_by('-id')
    cars = Car.objects.all().order_by('-id')
    context = {
        "brands": brands,
        "cars": cars,
    }
    return render(request, 'index.html', context)


def detail(request, slug):
    car = Car.objects.get(slug=slug)
    comments = Comment.objects.filter(car=car).order_by('-id')
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.car = car
            instance.save()
            return redirect(f'/detail/{slug}')
    else:
        form = CommentForm()
    context = {
        'object': car,
        'form': form,
        'comments': comments
    }
    return render(request, 'detail.html', context)

