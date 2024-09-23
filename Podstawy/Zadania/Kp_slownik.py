stolice = {
    "Poland": "Warsaw",
    "Germany": "Berlin",
    "Austria": "Vienna"}
print(stolice)
print(stolice.get("Austria"))
stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}}
print(stocks["TEN"]["Ten Square Games"])
stocks["BBT"] = {"Boombit": 23}
print(stocks.values())
project_ids = {'01': 'open',
               '03': 'in progress',
               '05': 'in progress',
               '04': 'completed'}
unique_statuses = list(set(project_ids.values()))
unique_statuses.sort()
print(unique_statuses)
profile = {'name': 'John Doe',
           'age': 25,
           'location': 'New York',
           'intersets': ['photography', 'music', 'hiking']}
profile["location"] = "Los Angeles"
profile["intersets"].append("Travel")
print(profile)
hotel_booking = {'hotel_name': 'Sheraton',
                 'check_in_date': '2024-06-10',
                 'check_out_date': '2023-06-13',
                 'room_type': 'Deluxe',
                 'num_guests': 2}
hotel_booking["num_guests"] = 3
hotel_booking["price"] = 200
del hotel_booking["room_type"]
num_keys = len(hotel_booking)
sorted_keys = sorted(hotel_booking.keys())
print(num_keys)
print(sorted_keys)
itinerary = {'destination': 'Paris, France',
             'duration': 7,'budget': 1500,
             'activities': ['Visit the Eiffel Tower','Explore the Louvre','Take a Seine River Cruise',]}
itinerary["duration"] = 10
itinerary["activities"].append("Visit the Palace of Versallies")
itinerary["accomodation"] = "Hotel"
print(f"Destination: {itinerary['destination']}")
print(f"Duration: {itinerary['duration']} days")
print(f"Budget: {itinerary['budget']}")
print(f"Number of activities: {len(itinerary['activities'])}")
team = {'name': 'Lakers',
        'city': 'Los Angeles',
        'players': {'LeBron James': {'position': 'Forward', 'number': 23, 'height': 203, 'weight': 113},
                    'Anthony Davis': {'position': 'Center', 'number': 3, 'height': 208, 'weight': 115,},
                    'Russell Westbrook': {'position': 'Guard', 'number': 0, 'height': 190, 'weight': 91}}}
lebron_weight = team["players"]["LeBron James"]["weight"]
print(f"LeBron James weights {lebron_weight} kg.")
team["players"]["Anthony Davis"]["number"] = 23
anthony = team["players"]["Anthony Davis"]
print(f"Team: {team['name']} - Anthony Davis ({anthony['position']})" f"#{anthony['number']}")