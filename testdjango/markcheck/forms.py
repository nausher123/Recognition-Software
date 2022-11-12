from calendar import month
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import ThresholdData


class ThresholdForm(forms.Form):
    subject= forms.CharField(initial= "enter your subject here")
    variant= forms.IntegerField(initial= "choose your variant")
    marks= forms.IntegerField(initial= "enter your marks")
    year= forms.ChoiceField(choices=[(2019,'2019'), (2020,'2020'), (2021, '2021'), (2022,'2022')])

class ThresholdForm1(forms.Form):
    subject= forms.ChoiceField(choices=[('math','Mathematics'), ('physics', 'Physics')], )
    variant= forms.IntegerField(min_value=0,widget=forms.TextInput(attrs={'placeholder': 'e.g 12,32'}))
    month= forms.ChoiceField(choices=[("M/J","M/J"),("O/N","O/N"),("F/M","F/M")], widget= forms.RadioSelect)
    year= forms.ChoiceField(choices=[(2019,'2019'), (2020,'2020'), (2021, '2021'), (2022,'2022')])
    
    marks= forms.IntegerField(min_value=0, required=False)
    

# make sure to put required = false btw

class SatForm(forms.Form):
    practice_test= forms.ChoiceField(choices= [('1','1'), ('2','2'), ('3','3') , ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'), ('9','9'), ('10','10')])
    incorrect_in_math= forms.IntegerField(required= False, min_value=0, max_value=58)
    incorrect_in_reading= forms.IntegerField(required= False, min_value=0, max_value=52)
    incorrect_in_writing= forms.IntegerField(required= False, min_value=0, max_value=44)
