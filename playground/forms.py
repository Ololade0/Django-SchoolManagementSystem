from django.forms import ModelForm

from playground.models import School, Student


class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'


class MyUserCreationForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['school']

