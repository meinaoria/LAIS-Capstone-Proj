from django import forms

from .models import bridgeTable, Elevators, Escalators, message

class bridgeTableForm(forms.ModelForm):
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

