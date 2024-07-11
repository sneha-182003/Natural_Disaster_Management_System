from django.shortcuts import render, redirect, get_object_or_404
from .forms import DisasterUpdateForm
from .models import DisasterUpdate

def index(request):
    updates = DisasterUpdate.objects.all().order_by('-date_reported')
    return render(request, 'index.html', {'updates': updates})

def add_update(request):
    if request.method == 'POST':
        form = DisasterUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DisasterUpdateForm()
    return render(request, 'add_update.html', {'form': form})

def disaster_detail(request, disaster_id):
    disaster = get_object_or_404(DisasterUpdate, pk=disaster_id)
    return render(request, 'disaster_detail.html', {'disaster': disaster})




