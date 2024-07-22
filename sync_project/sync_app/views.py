from django.shortcuts import render
from django.http import HttpResponse
from .forms import SyncForm
from .utils import synchronize_files 

def sync_view(request):
    if request.method == 'POST':
        form = SyncForm(request.POST) 
        if form.is_valid():
            source_server = form.cleaned_data['source_server']
            source_folder = form.cleaned_data['source_folder']
            destination_server = form.cleaned_data['destination_server']
            destination_folder = form.cleaned_data['destination_folder']

            # Call the synchronization function
            synchronize_files(source_server, source_folder, destination_server, destination_folder)
             
            return HttpResponse("Synchronization complete!")
    else:
        form = SyncForm()

    return render(request, 'sync_app/sync.html', {'form': form})
