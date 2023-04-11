person = {"name":"Ibrahim Aliyu", "age":5, "friends":['Ahmad', 'Isa']}

print(person)

# person.clear()
print(person.pop('friends'))
print(person)

person["hobbies"] = ["Football", "Eating"]
person["mother"] = "Hadiza"
person["father"] = "Musa"
print(person.get("age"))