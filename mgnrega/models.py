from django.db import models

class DistrictPerformance(models.Model):
    state_name = models.CharField(max_length=100, default='Maharashtra')
    district_name = models.CharField(max_length=100)
    financial_year = models.CharField(max_length=10)
    month = models.CharField(max_length=20)
    total_households_applied = models.IntegerField(default=0)
    total_households_allotted = models.IntegerField(default=0)
    total_persondays_generated = models.BigIntegerField(default=0)
    total_expenditure = models.BigIntegerField(default=0)  # In rupees
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('district_name', 'financial_year', 'month')
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.district_name} - {self.month} {self.financial_year}"