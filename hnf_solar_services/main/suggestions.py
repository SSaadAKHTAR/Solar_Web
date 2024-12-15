import math

# Solar panel wattages
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

def calculate_plates(totalLoad):
    suggestions = {}

    # Calculate plate requirements for each solar panel type
    for panel_name, wattage in solar_panels.items():
        plate_count = math.ceil(totalLoad / wattage)  # Round up to the nearest integer
        total_watts_generated = plate_count * wattage

        # Store the results
        suggestions[panel_name] = {
            "plate_count": plate_count,
            "total_watts_generated": total_watts_generated
        }

    return suggestions


# def main(totalLoad):
#     results = calculate_plates(totalLoad)

#     print("### Suggestions for Solar Panel Configuration ###\n")
#     for panel_name, data in results.items():
#         print(f"For {solar_panels[panel_name]}W panels:")
#         print(f"  Total plates required: {data['plate_count']}")
#         print(f"  Total watts generated: {data['total_watts_generated']}W\n")


# # Example totalLoad usage for manual testing
# if __name__ == "__main__":
#     totalLoad = 5000  # Replace with a dynamic value from calc.js/views.py
#     main(totalLoad)
