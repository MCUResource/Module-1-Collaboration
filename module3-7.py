things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
print(things)
# yes it changed the element in the list
things[0] = things[0].upper()
print(things)
del things[2]
print(things)
