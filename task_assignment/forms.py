from django import forms
from task_assignment.models import Contributor, Task, Attendance

class ContributorForm(forms.ModelForm):
    class Meta:
        model = Contributor
        fields = ['name', 'email']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Name'
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': '  Enter Email'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['contributor', 'title', 'start', 'end', 'is_completed']

        widgets = {
            'contributor': forms.Select(attrs={
                'class': 'form-control'
                }),
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter Task Title'
                }),
            'start': forms.DateTimeInput(attrs={
                'class': 'form-control', 
                'type': 'datetime-local'
                }),
            'end': forms.DateTimeInput(attrs={
                'class': 'form-control', 
                'type': 'datetime-local'
                }),
            'is_completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
                }),
        }

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['contributor', 'date', 'status']

        widgets = {
            'contributor': forms.Select(attrs={
                'class': 'form-control'
                }),
            'date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
                }),
            'status': forms.Select(attrs={
                'class': 'form-control'
                }),
        }