from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Graphic

# Create your views here.

def all_graphics(request):
    """ A view to show all graphics, including sorting and search queries """

    graphics = Graphic.objects.all()
    query = None
    
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('graphics'))

            # force an OR of queries otherwise search will look for AND of queries
            # | for OR and i in icontains for case insensitive
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            graphics = graphics.filter(queries)

    context = {
        'graphics': graphics,
        'search_term': query,
    }

    return render(request, 'graphics/graphics.html', context)


def graphic_detail(request, graphic_id):
    """ A view to show individual graphic details """

    graphic = get_object_or_404(Graphic, pk=graphic_id)

    context = {
        'graphic': graphic,
    }

    return render(request, 'graphics/graphic_detail.html', context)
