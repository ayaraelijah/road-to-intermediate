country = input("Enter your Country name: ")
visits = int(input("Enter the number of times you have visited the country: "))
list_of_cities = list(input("Enter the names of cities you have been to in that country: "))

travel_log = [
    {
        "country": "France",
        "visits": 10,
        "list_of_cities": ["paris","lille","monaco"]
    },

    {   "country": "England",
        "visits": 2,
        "list_of_cities": ["manchester", "chelsea", "london"]
    }
]

def add_country(name, no_of_times, no_of_cities):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = no_of_times
    new_country["list_of_cities"] = no_of_cities
    travel_log.append(new_country)

add_country(country, visits, list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} time(s)  ")

print(f"lists of cities you have visited are {travel_log[2]['list_of_cities']}")

