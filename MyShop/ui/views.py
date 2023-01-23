from django.shortcuts import render, redirect
from .forms import AddIdForm
from subprocess import Popen


def index(request):
    if request.method == "POST":
        form_add_id = AddIdForm(request.POST)
        if form_add_id.is_valid():
            string_id = form_add_id.save()
            form_add_id.save()
            Popen(['python', 'scraper.py', f'{string_id.id}'])
            return redirect('ui:index')

    form_add_id = AddIdForm()
    return render(request, 'ui/index.html', {'form_add_id': form_add_id})

