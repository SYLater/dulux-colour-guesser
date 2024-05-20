import json
from bs4 import BeautifulSoup

# Load the HTML content from the file
with open("Dulux-colours/all_dulux_colours.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the colour groups
colour_groups = soup.find_all("li", class_="colour-atlas-group__accordion__item")

# Initialize a dictionary to store all the colour information
all_colours = {}

# Iterate over each colour group
for group in colour_groups:
    group_name = group.find("span").text.strip()
    colours = []
    
    # Find all the colour items within the group
    colour_items = group.find_all("li", class_="colour-atlas-tile__item")
    
    for item in colour_items:
        button = item.find("button")
        colour_name = button.find("span").text.strip()
        colour_code = button.find("small").text.strip()
        
        # Extract the RGB values from the background-color style
        style = button.get("style")
        rgb_values = style.split("rgb(")[1].split(")")[0].split(", ")
        rgb = {
            "R": int(rgb_values[0]),
            "G": int(rgb_values[1]),
            "B": int(rgb_values[2])
        }
        
        # Create a dictionary for the current colour
        colour = {
            "name": colour_name,
            "code": colour_code,
            "rgb": rgb
        }
        
        # Add the colour to the list of colours in the current group
        colours.append(colour)
    
    # Add the current group and its colours to the main dictionary
    all_colours[group_name] = colours

# Save the dictionary to a JSON file
output_file = "Dulux-colours/colours.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(all_colours, file, ensure_ascii=False, indent=4)

print(f"Colours have been successfully extracted and saved to {output_file}.")
