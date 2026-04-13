trip = {
    "trip_id":"UB123",
    "pick_up":"hopes",
    "drop":["Airport","Thambaram","Church","Beach"],
    "Fare":400,
    "driver_name":"Ramesh",
    "trip_id":"UB1234" #this will be the new value for the key trip id
}

trips = [
    {
        "trip_id":"UB123",
        "pick_up":"hopes" },
    {
        "trip_id":"UB124",
        "pick_up":"Airport"
    }
]

tripsdict= {
    "First_trip":{"trip_id":"UB123","pick_up":"hopes" },
    "Second_trip":{"trip_id":"UB124","pick_up":"Airport"},
    "Third_trip": {"trip_id": "UB124", "pick_up": "Beach"}
}


print(trip)
print(trip["pick_up"])
print(trip.get("Airport"))
print(trip.keys())
print(trip.values())

for key,value in trip.items():
    print(f"{key}: {value}")

trip.update({"car_model":"Benz"})
print(trip) #If key car model present then it will update or else it will add the new key and value pair

trip.update({"car_model":"Audi"})
print(trip)

trip.pop("car_model")
print(trip)

for value in trip["drop"]:
    print(f"{value}")

for key,value in trip.items():
    if key=="drop":
        print(f"Key : drop -> {value}")
        for v in trip[key]:
            if v=="Airport":
                print("Required drop location ",v)

for trip in trips:
    print(trip["pick_up"]) #possible to access the dictionary inside a list also

for t,details in tripsdict.items():
    print(f"{t}: {details}")
    print(details["pick_up"])