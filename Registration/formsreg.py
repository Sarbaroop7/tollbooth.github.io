from django import forms
from django.contrib.auth.models import User

class UserRegDetails(forms.ModelForm):
    title = forms.CharField(max_length = 4)
    name = forms.CharField(max_length = 80)
    date_of_birth = forms.DateTimeField()
    address = forms.CharField(widget=forms.Textarea)
    city = forms.CharField(max_length = 50)
    state = forms.CharField(max_length = 50)
    nationality = forms.CharField(max_length = 60)
    car_number = forms.CharField(max_length = 80)
    timestamp = forms.DateTimeField()

    class Meta:
        model = User
        fields = ['title', 'email', 'date_of_birth',
                  'state', 'address', 'city', 'nationality', 'car_number', 'timestamp']
