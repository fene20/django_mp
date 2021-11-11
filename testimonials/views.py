from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def all_testimonials(request):
    """ A view that renders the (all) testimonials page """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'testimonials/all_testimonials.html', context)


def add_testimonial(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_testimonials') # Return to all_testimonials(request): above
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'testimonials/add_testimonial.html', context)


def edit_testimonial(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('all_testimonials')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'testimonials/edit_testimonial.html', context)


def delete_testimonial(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('all_testimonials') # Return to all_testimonials(request): above
