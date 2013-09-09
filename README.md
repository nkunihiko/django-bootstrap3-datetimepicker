django-bootstrap3-datetimepicker
================================

https://github.com/Eonasdan/bootstrap-datetimepicker
http://tarruda.github.io/bootstrap-datetimepicker/
http://www.eyecon.ro/bootstrap-datepicker/


Setup
-------------------------------

- Add 'bootstrap3_datetime' to your `INSTALLED_APPS`
- Set proper value for `STATIC_ROOT` and `STATIC_URL`
- Run `python manage.py collectstatic`
- 
	from django.conf.urls.static import static
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


Example
--------------------------------

###### forms.py
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


###### template.html
	<!DOCTYPE html>
	<html>
	    <head>
	        <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.css">
	        <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-theme.css">
	        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.js"></script>
	        <script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.js"></script>
	        {{ form.media }}
	    </head>
	    <body>
	        <form method="post" role="form">
	            {% for field in form.visible_fields %}
	            <div id="div_{{ field.html_name }}" class="form-group{% if field.errors %} has-error{% endif %}">
	                {{ field.label_tag }}
	                {{ field }}
	                <div class="text-muted pull-right"><small>{{ field.help_text }}</small></div>
	                <div class="help-block">
	                    {{ field.errors }}
	                </div>
	            </div>
	            {% endfor %}
	            {% for hidden in form.hidden_fields %}
	                {{ hidden }}
	            {% endfor %}
	            {% csrf_token %}
	            <div class="form-group">
	                <input name="confirm" type="submit" value="Submit" class="btn btn-primary" />
	            </div>
	        </form>
	    </body>
	</html>


