import pet2

p1 = pet2.pets[0]
p2 = pet2.Pet("Polly", ["cracker", "scurvy dog"])

print(p1.speak())
print(p2.speak())

pet2.teach_random(p1, 2)
pet2.teach_random(p2, 4)

print(p1.speak())
print(p2.speak())

print("In teach_pets.py, my name is", __name__)
