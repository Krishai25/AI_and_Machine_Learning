"""Tuple are immutable and only the methods count and index available """
trip_summary=("Uber","Coimbatore","Peelamedu",350.00,True)
print(trip_summary)

trip_summary2=("Uber","Coimbatore","Hopes",700.00,True)
print(trip_summary2)

new_trip_summary=trip_summary+trip_summary2
print(new_trip_summary)

new_trip_summary+=("Rating","5 star",)
print(new_trip_summary)
"""Adding the new members in the tuple"""

temp_list=list(new_trip_summary)
print(temp_list)
temp_list.append("List function")
print(temp_list) #Conversion of tuple to list and appending the members

trip=tuple(temp_list)
print(trip)  #Converting back to tuple after appending

print(new_trip_summary.count("Uber"))
print(new_trip_summary.index("hopes".capitalize()))
#Prints the first index of the Coimbatore found

for i,location in enumerate(new_trip_summary):
    if location=="Coimbatore":
        print(i,location)

