from django import forms
from .models import DisasterUpdate

class DisasterUpdateForm(forms.ModelForm):
    class Meta:
        model = DisasterUpdate
        fields = ['disaster_type', 'location', 'description', 'magnitude', 'affected_population', 'damage_cost']
