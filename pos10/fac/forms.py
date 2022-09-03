from django import forms

from .models import Barrio, Repartidor, Ruta, Cliente

class BarrioForm(forms.ModelForm):
    class Meta:
        model=Barrio
        #fields=[]
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class RutaForm(forms.ModelForm):
    class Meta:
        model=Ruta
        #fields=['nombre','descripcion','repartidor','estado']
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['repartidor'].empty_label =  "Seleccione Repartidor"

class RepartidorForm(forms.ModelForm):
    class Meta:
        model=Repartidor
        #fields=[]
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        #fields=[]
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['documento'].empty_label =  "No. de Documento"
        self.fields['barrio'].empty_label =  "Seleccione Barrio"
        self.fields['ruta'].empty_label =  "Seleccione Ruta"
