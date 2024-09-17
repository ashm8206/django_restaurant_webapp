from .models import Booking
from django.forms import ModelForm, DateInput


class BookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'reservation_time': DateInput(attrs={'type': 'date'}),
        }
