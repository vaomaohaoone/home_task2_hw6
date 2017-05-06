from django import forms
import datetime


class CreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    estimate = forms.DateField()

    def clean_estimate(self):
        estimate = self.cleaned_data['estimate']
        if estimate < datetime.date.today():
            raise forms.ValidationError("Дата меньше сегодняшней")
        if type(estimate) != type(datetime.datetime.date.today()):
            raise forms.ValidationError("Неверный тип даты")
        return estimate

    def clean_title(self):
        title = self.cleaned_data['title']
        if type(title) != type(''):
            raise forms.ValidationError("Неверный тип заголовка")


class EditForm(forms.Form):
    title = forms.CharField(max_length=100)
    state = forms.CharField(max_length=11)
    estimate = forms.DateField()

    def clean_estimate(self):
        estimate = self.cleaned_data['estimate']
        if estimate < datetime.date.today():
            raise forms.ValidationError("Дата меньше сегодняшней")
        if type(estimate) != type(datetime.date.today()):
            raise forms.ValidationError("Неверный тип даты")
        return estimate

    def clean_title(self):
        title = self.cleaned_data['title']
        if type(title) != type(''):
            raise forms.ValidationError("Неверный тип заголовка")

    def clean_state(self):
        state = self.cleaned_data['state']
        if state!='in_progress' and state!='ready':
            raise forms.ValidationError("Невалидный статус")
