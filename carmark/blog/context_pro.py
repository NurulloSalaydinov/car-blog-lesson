from .models import Brand


def get_brand(request):
    context = {
        'brands': Brand.objects.all().order_by('-id')
    }
    return context

