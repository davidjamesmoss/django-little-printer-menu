from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Dish, Setup


class SetupForm(forms.ModelForm):
    class Meta:
        model = Setup
        fields = ['menu_title', 'printer_key']

    def __init__(self, *args, **kwargs):
        super(SetupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form'

        self.helper.add_input(Submit('submit', 'Save', css_class='btn-lg'))


class DishesForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['title']

    def __init__(self, *args, **kwargs):
        super(DishesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        form_tag = False
        self.helper.form_class = 'form'

        self.helper.add_input(Submit('submit', 'Add', css_class='btn-lg'))
