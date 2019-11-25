from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import *
from django.urls import reverse

# bridge Form
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

# pca Form
class pcaTableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['PCA_Status_Choice'].widget.attrs['name'] = 'pcaChoice'

    class Meta:
        model = bridgeTable
        fields = [
            'PCA_Status_Choice',
        ]

# gpu Form
class gpuTableForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['GPU_Status_Choice'].widget.attrs['name'] = 'gpuChoice'

    class Meta:
        model = bridgeTable
        fields = [
            'GPU_Status_Choice',
        ]
 
  # elevator Form 
class elevatorForm(forms.ModelForm):
   # post =forms.CharField()
    class Meta:
        model = Elevators
        fields = [
            'Elevator_Status_Choice',
        ]

# escalator Form
class escalatorForm(forms.ModelForm):
   # post =forms.CharField()
    class Meta:
        model = Escalators
        fields = [
            'Escalator_Status_Choice',
        ]

# message Form
class messageForm(forms.ModelForm):
   # post =forms.CharField()
    class Meta:
        model = message
        fields = [
            'message',
        ]

# domIntBaggageSystem Form
class domIntBaggageSystemsForm(forms.ModelForm):
    class Meta:
        model = domIntBaggageSystems
        fields= [
            # 'domIntBaggageID',
            'DomIntBaggage_Status_Choice',
        ]

# tbBaggageSystem Form
class tbBaggageSystemsForm(forms.ModelForm):
    class Meta:
        model = tbBaggageSystems
        fields = [
            'TbBaggage_Status_Choice',
        ]

# tbOverSize Form
class tbOversizeForm(forms.ModelForm):
    class Meta:
        model = tbOversize
        fields = {
            'TbOversize_Status_Choice'
        }

# domIntOversize Form
class domIntOversizeForm(forms.ModelForm):
    class Meta:
        model = domIntOversize
        fields = {
            'DomIntOversize_Status_Choice'
        }

# bagCarousel Form
class bagCarouselForm(forms.ModelForm):
    class Meta:
        model = bagCarousel
        fields = {
            'bagCarousel_Status_Choice'
        }