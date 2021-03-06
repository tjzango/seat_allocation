from django import forms
from django.db import models
from django.db.models import fields
from .models import StaffSchedule, StudentBulkUpload, Venue, Staff, ScheduleExamination


class AdminLoginForm(forms.Form):
    admin_id = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Admin ID'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password'}))


class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = ('name', 'capacity')



class StaffScheduleForm(forms.ModelForm):

    class Meta:
        model = StaffSchedule
        fields = ('venue', 'exam')

class StaffForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Staff
        fields = ('staff_id',)


class VenueForm(forms.ModelForm):

    class Meta:
        model = Venue
        fields = ('name', 'capacity')


class StudentBulkUploadForm(forms.ModelForm):
    class Meta:
        model = StudentBulkUpload
        fields = ('session', 'csv_file')
        

class ScheduleExaminationForm(forms.ModelForm):

    class Meta:
        model = ScheduleExamination
        fields = ('name', 'exam_date', 'duration', "student_record")

class AddVenueForm(forms.Form):
    venue = forms.ModelChoiceField(
        required=True, queryset=Venue.objects.filter(show=True)
    )