# -*- coding: utf-8 -*-
from django.forms.util import flatatt
from django.forms.widgets import DateTimeInput
from django.utils import translation
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
import json
try:
    from django.utils.encoding import force_unicode as force_text
except ImportError: #python3
    from django.utils.encoding import force_text


class DateTimePicker(DateTimeInput):
    class Media:
        class _js_files(object):
            def __iter__(self):
                yield 'datetimepicker/js/bootstrap-datetimepicker.min.js'
                lang = translation.get_language()
                if lang and not lang.startswith('en'):
                    yield 'datetimepicker/js/locales/bootstrap-datetimepicker.{0}.js'.format(lang)
        js = _js_files()
        css = {'all': ('datetimepicker/css/bootstrap-datetimepicker.min.css',),}
    
    
    def __init__(self, attrs=None, format=None, options=None, div_attrs={'class': 'input-group date'}):
        super(DateTimePicker, self).__init__(attrs, format)
        if "class" not in self.attrs:
            self.attrs["class"] = "form-control"
        self.div_attrs = div_attrs and div_attrs.copy() or {}
        self.picker_id = self.div_attrs.get('id') or None
        if options == False: # do not initalize datetimepicker
            self.options = False
        else:
            self.options = options and options.copy() or {}
            self.options['language'] = translation.get_language()
        
    
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        input_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            input_attrs['value'] = force_text(self._format_value(value))
        input_attrs = {key: conditional_escape(val) for key, val in input_attrs.items()}
        if not self.picker_id:
            self.picker_id = input_attrs.get('id', '') + '_picker'
        self.div_attrs['id'] = self.picker_id
        picker_id = conditional_escape(self.picker_id)
        div_attrs = {key: conditional_escape(val) for key, val in self.div_attrs.items()}
        html = '''
                <div{div_attrs}>
                    <input{input_attrs} />
                    <span class="input-group-addon">
                        <span class="glyphicon glyphicon-calendar"></span>
                    </span>
                </div>'''.format(picker_id=picker_id,
                                 div_attrs=flatatt(div_attrs),
                                 input_attrs=flatatt(input_attrs))
        if self.options == False:
            js = ''
        else:
            options = json.dumps(self.options or {})
            js = '''
                <script>
                    $(function() {{
                        $('#{picker_id}').datetimepicker({options});
                    }});
                </script>'''.format(picker_id=picker_id, 
                                    options=options)
        return mark_safe(force_text(html + js))
    
    
    