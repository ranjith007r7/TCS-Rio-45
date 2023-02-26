from django import forms
from app30.models import Office
class OfficeForm(forms.ModelForm):
	class Meta:
		model=Office
		fields='__all__'