from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import *
from django.urls import reverse


class bridgeTableForm(forms.ModelForm):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['Bridge_Status_Choice'].widget.attrs['name'] = 'bridgeChoice'
      
       # post =forms.CharField()

   class Meta:
        model = bridgeTable
        fields = [
            'Bridge_Status_Choice',
        ]

class pcaTableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['PCA_Status_Choice'].widget.attrs['name'] = 'pcaChoice'

    class Meta:
        model = bridgeTable
        fields = [
            'PCA_Status_Choice',
        ]
class gpuTableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['GPU_Status_Choice'].widget.attrs['name'] = 'gpuChoice'

    class Meta:
        model = bridgeTable
        fields = [
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
class domIntBaggageSystemsForm(forms.ModelForm):
    class Meta:
        model = domIntBaggageSystems
        fields= [
            # 'domIntBaggageID',
            'DomIntBaggage_Status_Choice',
        ]

class tbBaggageSystemsForm (forms.ModelForm):
    class Meta:
        model = tbBaggageSystems
        fields = [
            'TbBaggage_Status_Choice',
        ]

class tbOversizeForm(forms.ModelForm):
    class Meta:
        model = tbOversize
        fields = {
            'TbOversize_Status_Choice'
        }

class domIntOversizeForm(forms.ModelForm):
    class Meta:
        model = domIntOversize
        fields = {
            'DomIntOversize_Status_Choice'
        }

class domIntPBSForm(forms.ModelForm):
    # post=forms.CharField()
    class Meta:
        model = domIntPBS
        fields = [
            'DomIntPBS_Status_Choice',
        ]

class tbPBSForm(forms.ModelForm):
    class Meta:
        model = tbPBS
        fields = {
            'TbPBS_Status_Choice'
        }



class electricalChargingForm(forms.ModelForm):
    class Meta:
        model = electricalCharging
        fields = {
            'ElectricalCharging_Status_Choice'
        }

class waterFillForm(forms.ModelForm):
    class Meta:
        model = waterFill
        fields = {
            'WaterFill_Status_Choice'
        }