from django.shortcuts import render, get_object_or_404
from .models import Graphic

# Create your views here.

def all_graphics(request):
    """ A view to show all graphics, including sorting and search queries """

    graphics = Graphic.objects.all()

    context = {
        'graphics': graphics,
    }

    return render(request, 'graphics/graphics.html', context)


def graphic_detail(request, graphic_id):
    """ A view to show individual graphic details """

    graphic = get_object_or_404(Graphic, pk=graphic_id)

    context = {
        'graphic': graphic,
    }

    return render(request, 'graphics/graphic_detail.html', context)
