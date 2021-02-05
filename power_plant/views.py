from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import System, Entry
from .forms import SystemForm,EntryForm

# Create your views here.

def index(request):

    return render(request, 'power_plant/index.html')

def systems(request):

    systems = System.objects.order_by('date_added')
    context = {'systems':systems}
    return render(request, 'power_plant/systems.html', context)

def system(request, system_id):

    system = System.objects.get(id=system_id)
    entries = system.entry_set.order_by('-date_added')
    context = {'system':system, 'entries':entries}
    return render(request, 'power_plant/system.html', context)

def new_system(request):

    if request.method != 'POST':
        form = SystemForm()
    else:
        form = SystemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('power_plant:systems'))

    context = {'form':form}
    return render(request, 'power_plant/new_system.html', context)

def new_entry(request, system_id):

    system = System.objects.get(id=system_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.system = system
            new_entry.save()
            return HttpResponseRedirect(reverse('power_plant:system',
                                                args=[system_id]))
    context = {'system': system, 'form': form}
    return render(request, 'power_plant/new_entry.html', context)

def edit_entry(request, entry_id):

    entry = Entry.objects.get(id=entry_id)
    system = entry.system

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('power_plant:system', args=[system.id]))

    context = {'entry':entry, 'system':system, 'form':form}
    return render(request, 'power_plant/edit_entry.html', context)
