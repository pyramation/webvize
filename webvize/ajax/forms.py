from django import forms
from cms.models import *

class TextField(forms.Field):
    def __init__(self, required, label, initial, widget, help_text):
        self.required = required
        self.label = label
        self.initial = initial
        self.widget = widget
        self.help_text = help_text
        super(TextField, self).__init__(required, label, initial, widget, help_text)

    def clean(self, value, initial=None):
        value = super(TextField, self).clean(value)
        return value

class ModifyPageForm(forms.Form):
    page = forms.ModelChoiceField(queryset=Page.objects.all())
    content = forms.CharField(max_length=10000000)

class DeletePageForm(forms.Form):
    page = forms.ModelChoiceField(queryset=Page.objects.all())


