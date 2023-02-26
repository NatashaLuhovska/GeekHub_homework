from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import AddIdForm
from .tasks import add_product


def index(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to access this page. Only for the site administrator.')
        return redirect(reverse('products:list'))
    if request.method == "POST":
        form_add_id = AddIdForm(request.POST)
        if form_add_id.is_valid():
            string_id = form_add_id.save()
            form_add_id.save()
            print(string_id.id)
            add_product.delay(string_id.id)
            return redirect('ui:index')

    form_add_id = AddIdForm()
    return render(request, 'ui/index.html', {'form_add_id': form_add_id})

