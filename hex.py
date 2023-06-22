import string

def generate_all_unique_hexcodes():
    hexcodes = set()
    characters = string.hexdigits.upper()  # Includes uppercase letters A-F and digits 0-9

    for char1 in characters:
        for char2 in characters:
            for char3 in characters:
                for char4 in characters:
                    for char5 in characters:
                        for char6 in characters:
                            hexcode = char1 + char2 + char3 + char4 + char5 + char6
                            hexcodes.add(hexcode)

    return hexcodes


all_unique_hexcodes = generate_all_unique_hexcodes()

# Save hexcodes to a file
filename = "hexcodes.txt"
with open(filename, "w") as file:
    for hexcode in all_unique_hexcodes:
        file.write("#" + hexcode + "\n")

print(f"All unique hexcodes saved to {filename}.")
