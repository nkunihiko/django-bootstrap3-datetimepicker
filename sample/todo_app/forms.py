from bootstrap3_datetime.widgets import DateTimePicker
from django import forms

class ToDoForm(forms.Form):
	todo = forms.CharField(
		widget=forms.TextInput(attrs={"class": "form-control"}))
	date = forms.DateField(
		widget=DateTimePicker(options={"format": "yyyy-MM-dd",
                                       "pickTime": False}))
	reminder = forms.DateTimeField(
		required=False,
		widget=DateTimePicker(options={"format": "yyyy-MM-dd hh:mm",
                                       "pickSeconds": False}))