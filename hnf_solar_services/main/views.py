from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# import math
from .suggestions import calculate_plates


solar_panels = {
    "solar1": 180,
    "solar2": 200,
    "solar3": 280,
    "solar4": 400,
    "solar5": 550,
    "solar6": 585,
    "solar7": 605,
    "solar8": 700, 
}

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def projects(request):
    return render(request, 'projects.html')

def blog(request):
    return render(request, 'blog.html')

def estimate_cost(request):  # Updated function name
    return render(request, 'solar_calc.html')

def suggestions_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)
            totalLoad = data.get('totalLoad')

            if totalLoad is None:
                return JsonResponse({"error": "No totalLoad provided"}, status=400)

            # Calculate suggestions
            results = calculate_plates(totalLoad)

            # Prepare response data
            response = {}
            for panel_name, panel_data in results.items():
                response[panel_name] = {
                    "wattage": solar_panels[panel_name],
                    "plate_count": panel_data["plate_count"],
                    "total_watts_generated": panel_data["total_watts_generated"]
                }

            return JsonResponse(response)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
