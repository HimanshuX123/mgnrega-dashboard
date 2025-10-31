from django.shortcuts import render
from django.http import JsonResponse
from .models import DistrictPerformance
import requests

def get_district_from_location():
    try:
        ip_resp = requests.get('https://api.ipify.org?format=json', timeout=5)
        ip = ip_resp.json()['ip']
        geo_resp = requests.get(f'http://ip-api.com/json/{ip}?fields=regionName,city', timeout=5).json()
        if geo_resp.get('regionName') == 'Maharashtra':
            return geo_resp.get('city', 'Pune')
    except:
        pass
    return None  # Fallback to manual select

def home(request):
    auto_district = get_district_from_location()
    districts = DistrictPerformance.objects.values_list('district_name', flat=True).distinct()
    return render(request, 'home.html', {
        'districts': list(districts),
        'auto_district': auto_district
    })

def district_data(request, district):
    data = list(DistrictPerformance.objects.filter(district_name=district).order_by('-financial_year', '-month')[:12].values())
    return JsonResponse(data, safe=False)
def comparison(request):
    # SAHI TARAH SE UNIQUE DISTRICTS
    districts = DistrictPerformance.objects.values_list('district_name', flat=True).distinct()
    total_districts = districts.count()  # YE 36 HOGA

    latest_data = DistrictPerformance.objects.filter(
        month__endswith='October 2024'
    ).values('district_name', 'total_persondays_generated', 'total_expenditure')

    # Top 5 by persondays
    top5 = sorted(latest_data, key=lambda x: x['total_persondays_generated'], reverse=True)[:5]

    return render(request, 'comparison.html', {
        'districts': districts,
        'top5': top5,
        'total_districts': total_districts  # YE 36 HOGA
    })