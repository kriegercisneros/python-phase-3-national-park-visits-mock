#!/usr/bin/env python3
# import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip


# Names of visitors
jackie = Visitor("Jackie")
print(jackie.name)
jackie.name="not jackie"
dylan = Visitor("Dylan")
abby = Visitor("Abby")


# National Parks
rocky_mountian = NationalPark("Rocky Mountain National Park")
bryce = NationalPark("Bryce National Park")
# rocky_mountian.name = "Zion"
obj = NationalPark(rocky_mountian)


# Trips
smith_family = Trip("Abby", "Rocky Mountain National Park", "Aug 3", "Aug 10")
smith_family = Trip("Abby", "Rocky Mountain National Park", "Aug 3", "Aug 10")

# print(Trip.all[0].visitor)
# print(obj)

# This is a way to break the hasattr relationship by passing in a location instead of a name
# print(hasattr(obj, "location"))
# This is a way to make hasatt by keeping name 
# print(hasattr(obj, "name"))
# print(jackie.name)
# print(rocky_mountian.name)
# if __name__ == '__main__':
#     print("HELLO! :) let's debug :vibing_potato:")

    # ipdb.set_trace()