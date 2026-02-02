"""
TODO:
Create and unpack a tuple
Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.
Unpack the tuple into three separate variables: lat, lon, and alt.
Create a tuple with mixed data types
Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).
Unpack the tuple into three separate variables: name, age, and height.
Demonstrate tuple immutability
Create a tuple named 'immutable_tuple' with three integer values.
Attempt to change the first element of the tuple to a different value and handle the exception that arises
"""


print("Create and unpack a tuple")
classes =("Data Structures", "Intro to Finance", "AI Elective")
class1, class2, class3=classes
print("Create a tuple named 'coordinates' that contains three values: latitude, longitude, and altitude.")
coordinates=("31.7767°N","35.2345°E","738")
lat, lon, alt=coordinates
print("Create a tuple with mixed data types")
city=("Far Rockaway", 11691)
print("Create a tuple named 'person_info' that contains a string (name), an integer (age), and a float (height).")
person_info=("Tehilla", 21,5.2)
name, age, height=person_info
immutableTuple=(1,2,3)
try:
    immutableTuple[0]=0
except TypeError as e:
    print(f"Error: {e}")
