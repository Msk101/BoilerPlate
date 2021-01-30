from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name','last_name','age','year_of_experience','nursing_qualification','german_language_level','document_url')
        labels = {
            'first_name':'First Name',
            'last_name' :'Last Name',
            'age':'Age',
            'year_of_experience':'Year Of Experience',
            'nursing_qualification':'Nursing Qualification',
            'german_language_level':'German Language Level',
            'document_url':'Upload Document'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['german_language_level'].empty_label = "Select Level"
        self.fields['document_url'].required = False
