from django import forms

from .models import bridgeTable, Elevators, Escalators, message

class bridgeTableForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['Bridge_Status_Choice'].widget.attrs['name'] = 'bridgeChoice'
       self.fields['PCA_Status_Choice'].widget.attrs['name'] = 'pcaChoice'
       self.fields['GPU_Status_Choice'].widget.attrs['name'] = 'gpuChoice'
       # post =forms.CharField()

   class Meta:
        model = bridgeTable
        fields = [
            'Bridge_Status_Choice',
            'PCA_Status_Choice',
            'GPU_Status_Choice',
        ]

class elevatorForm(forms.ModelForm):
   # post =forms.CharField()
    class Meta:
        model = Elevators
        fields = [
            'Elevator_Status_Choice',
        ]

class escalatorForm(forms.ModelForm):
   # post =forms.CharField()
    class Meta:
        model = Escalators
        fields = [
            'Escalator_Status_Choice',
        ]

class messageForm(forms.ModelForm):
   # post =forms.CharField()
    class Meta:
        model = message
        fields = [
            'message',
        ]

