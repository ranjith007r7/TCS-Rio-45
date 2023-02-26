from django import forms
from app26.models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields='__all__'