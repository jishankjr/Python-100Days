# f-strings

letter = "Hey, my name is {1} and I am from {0}"
country = "Nepal"
name = "Jishank"

print(letter.format(country, name))

print(f"Hey, my name is {name} and I am from {country}")
print(f"Hey, my name is {name} and I am from {country}")
print(f"Hey, my name is {{name}} and I am from {{country}}")

price = 49.09999
y = f"For only {price: .2f} dollars!"
print(y)

pr = "My name is {}"
print(pr.format("JR"))

print(f"2 * 30")
print(f"{2 * 30}")