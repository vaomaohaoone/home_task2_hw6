from django import forms
import datetime
from myapp.models import Task, RoadMap
from django.forms import ModelForm


class CreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'estimate', 'road_map']

    def clean_estimate(self):
        estimate = self.cleaned_data['estimate']
        if estimate < datetime.date.today():
            raise forms.ValidationError("Дата меньше сегодняшней")
        return estimate



class AnotherCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'estimate']

    def clean_estimate(self):
        estimate = self.cleaned_data['estimate']
        if estimate < datetime.date.today():
            raise forms.ValidationError("Дата меньше сегодняшней")
        return estimate



class CreateRoadMap(ModelForm):
    class Meta:
        model = RoadMap
        fields = ['rd_id', 'name']


class EditForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'estimate', 'state', 'road_map']

        def clean_estimate(self):
            estimate = self.cleaned_data['estimate']
            if estimate < datetime.date.today():
                raise forms.ValidationError("Дата меньше сегодняшней")
            return estimate

        def clean_state(self):
           state = self.cleaned_data['state']
           if state!='in_progress' and state!='ready':
               raise forms.ValidationError("Невалидный статус")
