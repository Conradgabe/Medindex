from django.shortcuts import render
from .forms import MedicRecordForm

def index(request):

    form = MedicRecordForm()

    if request.method == 'POST':
        form = MedicRecordForm(request.POST)
        if form.is_valid:
            form.save()
            
    context = {'form': form}
    return render(request, 'medics/base.html', context)

