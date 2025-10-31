# mgnrega/management/commands/fetch_mgnrega.py

import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand
from mgnrega.models import DistrictPerformance

class Command(BaseCommand):
    help = 'Load 36 Maharashtra districts with 6 months data'

    def handle(self, *args, **options):
        self.stdout.write("Loading 36 districts of Maharashtra...")

        # CLEAR OLD DATA (optional - only if you want fresh)
        # DistrictPerformance.objects.all().delete()

        if DistrictPerformance.objects.exists():
            self.stdout.write("Data already exists. Skipping...")
            return

        districts = [
            "Ahmednagar", "Akola", "Amravati", "Aurangabad", "Beed", "Bhandara",
            "Buldhana", "Chandrapur", "Dhule", "Gadchiroli", "Gondia", "Hingoli",
            "Jalgaon", "Jalna", "Kolhapur", "Latur", "Mumbai City", "Mumbai Suburban",
            "Nagpur", "Nanded", "Nandurbar", "Nashik", "Osmanabad", "Palghar",
            "Parbhani", "Pune", "Raigad", "Ratnagiri", "Sangli", "Satara",
            "Sindhudurg", "Solapur", "Thane", "Wardha", "Washim", "Yavatmal"
        ]

        base_date = datetime(2024, 10, 1)
        saved = 0

        for district in districts:
            for i in range(6):  # Last 6 months
                month_date = base_date - relativedelta(months=i)
                month_name = month_date.strftime("%B %Y")

                households_allotted = random.randint(5000, 15000)
                persondays = households_allotted * random.randint(25, 45)
                expenditure = persondays * random.randint(220, 280)

                DistrictPerformance.objects.create(
                    state_name="Maharashtra",
                    district_name=district,
                    financial_year="2024-2025",
                    month=month_name,
                    total_households_applied=households_allotted + random.randint(200, 800),
                    total_households_allotted=households_allotted,
                    total_persondays_generated=persondays,
                    total_expenditure=expenditure
                )
                saved += 1

        self.stdout.write(self.style.SUCCESS(f'36 DISTRICTS × 6 MONTHS = {saved} records loaded!'))