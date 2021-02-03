from .models import Pledge
from django import forms


class PledgeForm(forms.ModelForm):

    class Meta:
        model = Pledge
        fields = (
            "title",
            "current_meals",
            "veggie_meals",
            "energy_supplier",
            "number_of_people",
            "heating_source",
            "message",
        )
