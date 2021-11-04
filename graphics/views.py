from django.shortcuts import render
from .models import Graphic

# Create your views here.

def all_graphics(request):
    """ A view to show all graphics, including sorting and search queries """

    graphics = Graphic.objects.all()

    context = {
        'graphics': graphics,
    }

    return render(request, 'graphics/graphics.html', context)