from django.db import models
from django.contrib.auth.models import User


class Pledge(models.Model):

    BOG_STANDARD = 'BS'
    A_GREAT_GREEN_TARRIF = 'GT'
    energy_supplier_choices = [
        (BOG_STANDARD, 'bog standard'),
        (A_GREAT_GREEN_TARRIF, 'a great green tarif'),
    ]
    energy_supplier = models.CharField(
        max_length=2,
        choices=energy_supplier_choices,
        default=BOG_STANDARD
    )

    GAS_OR_OIL = 'GO'
    ELECTRICITY = 'EL'

    heating_source_choices = [
        (GAS_OR_OIL, 'gas or oil'),
        (ELECTRICITY, 'electricity'),
    ]
    heating_source = models.CharField(
        max_length=2,
        choices=heating_source_choices,
        default=GAS_OR_OIL
    )

    title = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    current_meals = models.IntegerField()
    veggie_meals = models.IntegerField()
    number_of_people = models.IntegerField()
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
