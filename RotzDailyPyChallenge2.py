#1) Create a tuple called freshman_classes containing the values EET145, MTH181 and CIT160.
freshman_classes = ("EET145","MTH181","CIT160")
#· Assign each element of the tuple to the variable Class1, Class2, Class3. (you can actually assign them all at the same time)
Class1 = freshman_classes[0]
Class2 = freshman_classes[1]
Class3 = freshman_classes[2]
#· Print all three classes using their variables in sentence format, for example “Class 1 is: “, etc.
print(f"Class 1 is: {Class1} \nClass 2 is: {Class2} \nClass 3 is: {Class3}")
#2) Create a list called sophomore_classes with the values of CIT241, CIT240 and CIT246.
sophomore_classes = ['CIT241', 'CIT240', 'CIT246']
#· Print the Length of the list
print(len(sophomore_classes))
#· Append the class IAS312 to the end of the list
sophomore_classes.append("IAS312")
#· Insert the class MGT115 at index 1 in the list
sophomore_classes.insert(1,"MGT115")
#· Print the new list
print(sophomore_classes)
#· Remove CIT241 from the list
sophomore_classes.remove("CIT241")
#· Pop CIT246 from the list
sophomore_classes.pop(2)
#· Print the list
print(sophomore_classes)
#· Clear the entire list contents but keep the list itself
sophomore_classes.clear()
#· Print the empty list
print(sophomore_classes)
#3) Create a dictionary called lunch with the keys and values of:
#Drink Unsweet Tea
#Entree Sandwich
#Side Salad
lunch = {
    'Drink': "Unsweet Tea",
    'Entree': "Sandwich",
    'Side': "Salad"
}
#· Print the newly created dictionary
print(lunch)
#· Print just the keys
print(lunch.keys())
#· Print just the values
print(lunch.values())
#· Update the list and add dessert of cookie
lunch.update({'Dessert': "Cookie"})
print()
#4) Create a nested dictionary called garage. The top level will contain the keys of First, Second, Third. The nested dictionary will contain the keys and values as follows (if you want to use your own values that’s fine):

#First
#Make VW
#Year 2000
#Model Jetta

#Second
#Make Ford
#Year 1998
#Model F150

#Third
#Make Chevy
#Year 2005
#Model Silverado
garage = {
    "First": {
        "Make": 'VW',
        "Year": '2000',
        "Model": 'Jetta'
    },
    "Second": {
        "Make": "Ford",
        "Year": "1998",
        "Model": "F150"
    },
    "Third": {
        "Make": "Chevy",
        "Year": "2005",
        "Model": "Silverado"
    }
}
#· Print the Make from the First car in the garage
print(garage["First"]["Make"])
#· Print the Year of the Second card in the garage
print(garage["Second"]["Year"])
#· Print the Model of the Third car in the garage
print(garage["Third"]["Model"])
print()
#5) Iterate through Garage First values using a loop and print the results.
for key in garage["First"]:
    print(garage["First"][key])

#6) Create a separate python file called module1.py.
#· Create a function inside the module file called my_info that prints your name, age, and favorite color.
#· Import and call module1 from your main script file (this may require you to select the current folder in VSCode if you haven’t done this yet)
print()
import module1
module1.my_info()

#7) Install a 3rd party python package to covert the following markdown string to HTML
markdown_string = '''# Important packages 
- requests 
- numpy 
- sqlalchemy
'''
import markdown
html = markdown.markdown(markdown_string)
#· Print the new HTML string
print(html)
#8) Look through the wide verify of 3rd party modules and packages offered in Python. Locate one that interests you that I did not specifically mention in the slides. Give me its name and describe what it can do.

# pypdf is a package that allows you to modify PDF files and extract data from them. It can retrieve text and metadata, add a password, or merge PDF files together.