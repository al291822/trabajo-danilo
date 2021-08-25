from django.forms import ModelForm
from .models import Producto

class agregar_producto_form(ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'