from django import forms

from .models import bridgeTable, Elevators, Escalators, message, domIntPBS,\
    domIntBaggageSystems, tbPBS, tbBaggageSystems, tbOversize, domIntOversize, \
    lavHut, electricalCharging, waterFill

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

class lavHutForm(forms.ModelForm):
    class Meta:
        model = lavHut
        fields = {
            'LavHut_Status_Choice'
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