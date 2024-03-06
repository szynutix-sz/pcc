#!/usr/bin/env python3.10

# first_name = "ada"
# last_name = "lovelace"

# full_name = f"{first_name} {last_name}"
# print(f"Hello, {full_name.title()}")

# message = "  Languages:\n\tPython\n\tJava\n\tJavaScript    "
# print(message)

# message = message.strip()
# print(message)

# google_url = "https://www.google.com"
# simple_url = google_url.removeprefix("https://")
# print(simple_url)

first_name = "szymon"
last_name = "bar"

print(f"Hello {first_name.title()}! Come with me to learn some Python!")

full_name = f"{first_name} {last_name}"
print(f"{full_name.lower()}\n{full_name.upper()}\n{full_name.title()}")

famous_person = "alber einstein"
message = f'{famous_person.title()} once said "A person who never makes a mistake never tried anything new"'
print(message)

full_name = "\n\t\tszymon\nbar\t\n"
print(full_name)
print(full_name.rstrip())
print(full_name.lstrip())
print(full_name.strip())

file_name = "python.txt"
print(file_name.removesuffix(".txt"))
print(file_name.removesuffix(".jpg"))
