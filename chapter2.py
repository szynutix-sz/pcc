#!/usr/bin/env python3.10

first_name = "ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")

message = "  Languages:\n\tPython\n\tJava\n\tJavaScript    "
print(message)

message = message.strip()
print(message)

google_url = "https://www.google.com"
simple_url = google_url.removeprefix("https://")
print(simple_url)
