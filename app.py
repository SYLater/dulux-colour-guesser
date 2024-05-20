from flask import Flask, render_template, jsonify
import json

# Initialize Flask app
app = Flask(__name__)

# Load colour data from JSON file with utf-8 encoding
with open('Dulux-colours/colours.json', 'r', encoding='utf-8') as f:
    colour_data = json.load(f)

# Extract colour names and their corresponding RGB values along with the group name
colour_list = []
for group, colours in colour_data.items():
    for colour in colours:
        colour_name = colour.get('name')
        rgb_values = colour.get('rgb')
        colour_list.append({
            'name': colour_name,
            'rgb': rgb_values,
            'group': group
        })

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve the colour data as JSON
@app.route('/colours')
def get_colours():
    return jsonify(colour_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
