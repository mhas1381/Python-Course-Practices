travel_log = [
    {"country": "Russia",
     "visits": 12,
     "cities": ["leningrad", "moscow", "stalingrad"]},
    {
        "country": "America",
        "visits": 6,
        "cities": ["pensilvania", "Washington", "chicago"],
    }
]


def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})


add_new_country("brazil", 3, ["test", "test2"])

print(travel_log)
