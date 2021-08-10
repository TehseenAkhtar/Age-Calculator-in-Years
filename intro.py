a = "Hello Jucifer Ali"
print(a)
print(a[:5])
print(a[6:])
print(a.lower())
print(a.upper())
print(a.count("j"))
print(a.count("J"))
print(a.find("Ali"))  # return index of find message
new_a = a.replace("Jucifer", "Tehseen")
print(new_a)
print("The length of string is: ")
print(len(a))

both = a + " and " + new_a
print(both)
both2 = "{}. and {}. ".format(a, new_a)
print(both2)
both3 = f"{a}. and {new_a}. "
print(both3)
