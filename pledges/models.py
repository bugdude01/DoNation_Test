from django.db import models
from django.contrib.auth.models import User


class Pledge(models.Model):

    title = models.CharField(max_length=100)
    current_meals = models.IntegerField()
    veggie_meals = models.IntegerField()

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

    number_of_people = models.IntegerField()

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

    message = models.TextField(max_length=255, blank=True)
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
