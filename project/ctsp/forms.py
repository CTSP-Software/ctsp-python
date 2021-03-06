from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Project, User, US
from django.contrib import messages
from enum import Enum

# Create your forms here.

'''
This module contains the forms logic for the whole application.
Django forms are used to manipulate the data coming from the browser into the data going into the application logic or database.
Django forms can also interact with HTML while making data ready to be received.
To learn more about Django forms refer to: https://docs.djangoproject.com/en/2.0/topics/forms/
'''


class ProjectForm(forms.ModelForm, forms.Form):
    project_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label='Project Name', max_length=Project.project_name_max_length)

    project_start_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control control-label', 'id': 'start_date', 'placeholder': "MM/DD/YYY",
            'autocomplete': 'off',
        }
    ), label='Start date')

    project_final_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control control-label', 'id': 'final_date', 'placeholder': "MM/DD/YYY",
            'autocomplete': 'off',
        }
    ), label='Final date')

    class Meta:
        model = Project
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('project_start_date')
        final_date = cleaned_data.get('project_final_date')
        if start_date and final_date:
            if final_date < start_date:
                raise forms.ValidationError("string error")
            return cleaned_data


class UserForm(forms.Form):
    nome = forms.CharField(required=True)
    sobrenome = forms.CharField(required=True)
    data = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    habilidades = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    confirmsenha = forms.CharField(required=True)

    def is_valid(self):
        valid = True

        if not super(UserForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados')
            valid = False

        user_exists = User.objects.filter(email=self.data['email']).exists()

        if user_exists:
            self.adiciona_erro('Esse email ja foi cadastrado')
            valid = False

        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(
            forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)


class QueryProjectForm(forms.ModelForm):
    project_name_or_ID = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'id': 'project_name_or_ID'
        }
    ), label='Project Name or ID', max_length=Project.project_name_max_length)

    class Meta:
        model = Project
        fields = ('project_name_or_ID',)


class USRegister(forms.ModelForm):
    # us_project = forms.IntegerField()

    us_title = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'us_title', 'placeholder': 'US Title'
        }
    ), label="US Name", max_length=US.us_title_max_length)

    us_estimative = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            "label": "number"
        }
    ), label="Estimative in days")

    us_type = forms.ChoiceField(widget=forms.Select(
        attrs={
            'id': 'us_type'
        }
    ), label="US Type", choices=US.us_type_choices)

    us_priority = forms.ChoiceField(widget=forms.Select(
        attrs={
            'id': 'us_priority'
        }
    ), label="Priority", choices=US.us_priority_choices)

    us_description = forms.CharField(widget=forms.Textarea(
        attrs={
            'id': 'us_description', 'placeholder': "US Description", 'rows': '4', 'cols': '50'
        }
    ), label='US Description', max_length=US.us_description_max_length)

    us_acceptance = forms.CharField(widget=forms.Textarea(
        attrs={
            'id': 'us_acceptance', 'placeholder': "US Acceptance Criteria", 'rows': '4', 'cols': '50'
        }
    ), label='US Description', max_length=US.us_acceptance_max_length)

    class Meta:
        model = US
        exclude = ('us_project',)
