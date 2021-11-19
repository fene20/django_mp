from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Graphic, Category
from .forms import GraphicForm

# Create your views here.

def all_graphics(request):
    """ A view to show all graphics, including sorting and search queries """

    graphics = Graphic.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                # Copying the sort parameter into a new variable called sortkey.
                # This preserves the original field we want it to sort on - name.
                # The actual field we're going to sort on is lower_name in the sort key variable.
                # If we had just renamed sort itself to lower_name we would have lost the original field name.
                # annotate adds on the new field.
                graphics = graphics.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    # minus to reverse order
                    sortkey = f'-{sortkey}'
            graphics = graphics.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # double underscore when looking for access to name field of category model
            # converting the list of strings of category names passed through the URL into a list of actual category objects, so that we can access all their fields in the template.
            graphics = graphics.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('graphics'))

            # force an OR of queries otherwise search will look for AND of queries
            # | for OR and i in icontains for case insensitive
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            graphics = graphics.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'graphics': graphics,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'graphics/graphics.html', context)


def graphic_detail(request, graphic_id):
    """ A view to show individual graphic details """

    graphic = get_object_or_404(Graphic, pk=graphic_id)

    context = {
        'graphic': graphic,
    }

    return render(request, 'graphics/graphic_detail.html', context)


def add_graphic(request):
    """ Add a graphic to the store """
    if request.method == 'POST':
        form = GraphicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added graphic!')
            return redirect(reverse('add_graphic'))
        else:
            messages.error(request, 'Failed to add graphic. Please ensure the form is valid.')
    else:
        form = GraphicForm()
        
    template = 'graphics/add_graphic.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
