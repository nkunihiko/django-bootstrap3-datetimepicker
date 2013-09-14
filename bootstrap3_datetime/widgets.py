# -*- coding: utf-8 -*-
from django.forms.util import flatatt
from django.forms.widgets import DateTimeInput
from django.utils import translation
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
try:
    import json
except ImportError:
    from django.utils import simplejson as json
try:
    from django.utils.encoding import force_unicode as force_text
except ImportError: #python3
    from django.utils.encoding import force_text


class DateTimePicker(DateTimeInput):
    class Media:
        class _js_files(object):
            def __iter__(self):
                yield 'bootstrap3_datetime/js/bootstrap-datetimepicker.min.js'
                lang = translation.get_language()
                if lang and not lang.startswith('en'):
                    yield 'bootstrap3_datetime/js/locales/bootstrap-datetimepicker.%s.js' % (lang)
        js = _js_files()
        css = {'all': ('bootstrap3_datetime/css/bootstrap-datetimepicker.min.css',),}
    
    format_map = (('dd', r'%d'),
                  ('MM', r'%m'),
                  ('yyyy', r'%Y'),
                  ('yy', r'%y'),
                  ('ms', r'%f'), #NOTE: ms: milliseconds, %f: microseconds
                  ('hh', r'%H'),
                  ('mm', r'%M'),
                  ('ss', r'%S'),
                  ('HH', r'%I'),
                  ('PP', r'%p'),
                  )
    
    @classmethod
    def conv_datetime_format_py2js(cls, format):
        for js, py in cls.format_map:
            format = format.replace(py, js)
        return format
    
    @classmethod
    def conv_datetime_format_js2py(cls, format):
        for js, py in cls.format_map:
            format = format.replace(js, py)
        return format
    
    def __init__(self, attrs=None, format=None, options=None, div_attrs={'class': 'input-group date'}):
        if format is None and options and options.get('format'):
            format = self.conv_datetime_format_js2py(options.get('format'))
        super(DateTimePicker, self).__init__(attrs, format)
        if 'class' not in self.attrs:
            self.attrs['class'] = 'form-control'
        self.div_attrs = div_attrs and div_attrs.copy() or {}
        self.picker_id = self.div_attrs.get('id') or None
        if options == False: # datetimepicker will not be initalized
            self.options = False
        else:
            self.options = options and options.copy() or {}
            self.options['language'] = translation.get_language()
            if format and not self.options.get('format'):
                self.options['format'] = self.conv_datetime_format_py2js(format)
    
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        input_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            input_attrs['value'] = force_text(self._format_value(value))
        input_attrs = dict([(key, conditional_escape(val)) for key, val in input_attrs.items()]) # python2.6 compatible
        if not self.picker_id:
            self.picker_id = input_attrs.get('id', '') + '_picker'
        self.div_attrs['id'] = self.picker_id
        picker_id = conditional_escape(self.picker_id)
        div_attrs = dict([(key, conditional_escape(val)) for key, val in self.div_attrs.items()]) # python2.6 compatible
        html = '''
                <div%(div_attrs)s>
                    <input%(input_attrs)s/>
                    <span class="input-group-addon">
                        <span class="glyphicon glyphicon-calendar"></span>
                    </span>
                </div>''' % dict(div_attrs=flatatt(div_attrs),
                                 input_attrs=flatatt(input_attrs))
        if self.options == False:
            js = ''
        else:
            js = '''
                <script>
                    $(function() {
                        $("#%(picker_id)s").datetimepicker(%(options)s);
                    });
                </script>''' % dict(picker_id=picker_id, 
                                    options=json.dumps(self.options or {}))
        return mark_safe(force_text(html + js))
    
    
    