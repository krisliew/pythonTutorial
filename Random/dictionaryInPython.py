#Simple program playing with dictionary in Python
#A dictionary is an associative array (also known as hashes).
#  Any key of the dictionary is associated (or mapped) to a value. 
# The values of a dictionary can be any Python data type.

myDtn = {"age":19,"goals scored":888,"price":10000000}
print("Default Age:",myDtn["age"])

myDtn["age"] = 20
print("Updated Age:",myDtn["age"])

myDtn["favFood"] = "Fried Chicken!" #appending in "myDtn" dictionary
print(myDtn)

#Small Challenge: Set Drink2 to "Boba Tea", Answer is below...
myDictionary = ["Set Menu",{"Food1":"Nasi Lemak","Drink1":"Pearl Bandung"},{"Food2":"Cheese Nan","Drink2":""}]
print(myDictionary)

#Big Challenge: Print the "HEY" , Answer is below...
myDict = {"name":"Pasta","price":35,"blah":{"one":1,"two":[1,2,3,[{"Bro":"HEY"}]]}}


#Answer for Small Challenge
myDictionary[2]["Drink2"] = "Boba Tea"
print(myDictionary[2])

#Answer for Big Challenge
print(myDict["blah"]["two"][3][0]["Bro"])