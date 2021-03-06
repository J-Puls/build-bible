from django import forms
from django.apps import apps

Post = apps.get_model('content', 'Post')
Vehicle = apps.get_model('vehicles', 'Vehicle')
vehicles = Vehicle.objects.all()
m_choices = []
for v in vehicles:
    if (v.manufacturer, v.manufacturer) not in m_choices:
        m_choices.append((v.manufacturer, v.manufacturer))
m_choices = sorted(m_choices)
first_choice = m_choices[0][0]


class FindVehicleForm(forms.ModelForm):
    manufacturer = forms.ChoiceField(choices=m_choices)
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.filter(manufacturer=first_choice), empty_label='Choose Platform')
    class Meta:
        model = Vehicle
        fields = ['manufacturer']


class SearchForm(forms.ModelForm):
    query = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    class Meta:
        model = Post
        fields=['query']

from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
    
    def clean_author(self):
        if not self.cleaned_data['author']:
            return User()
        return self.cleaned_data['author']
    
    def clean_last_modified_by(self):
        if not self.cleaned_data['last_modified_by']:
            return User()
        return self.cleaned_data['last_modified_by']