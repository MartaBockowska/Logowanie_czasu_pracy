from django.forms import ModelForm
from .models import WorkingTime
from django.core.exceptions import ValidationError


class WorkingReportForm(ModelForm):
    class Meta:
        model = WorkingTime
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        arrival = cleaned_data.get("arrival")
        leaving = cleaned_data.get("leaving")

        if arrival > leaving:
            raise ValidationError(
                    "Arrival has to be lower than leaving"
            )