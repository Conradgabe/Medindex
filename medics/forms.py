from django.forms import ModelForm
from .models import MedicRecord

class MedicRecordForm(ModelForm):
    class Meta:
        model = MedicRecord
        fields = '__all__'