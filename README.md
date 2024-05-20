# Dulux Colour Guesser

The Dulux Colour Guesser is a web-based interactive game where players are challenged to guess colours based on their names. It uses a Flask backend to serve the game and provide functionality for loading and displaying colours.

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.6+
- Flask
- BeautifulSoup4

You can install the necessary dependencies by running:

```bash
pip install Flask BeautifulSoup4
```

### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. Clone the repository:
   ```bash
   git clone https://github.com/SYLater/dulux-colour-guesser.git
   cd dulux-colour-guesser
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python colour_guessing_game.py
   ```

4. Visit `http://localhost:5000` in your web browser to start playing the game.

## Project Structure

Here's a brief overview of the project files and directories:

- `colour_guessing_game.py`: The main Flask application script.
- `Dulux-colours/`:
  - `all_dulux_colours.html`: All Dulux colours extracted from their website.
  - `colours.json`: Contains the colour data extracted from Dulux colour charts.
  - `extract_colours.py`: A script to scrape Dulux colour data and save it as JSON.
- `templates/`:
  - `index.html`: The main HTML file for the Flask app, displaying the game interface.
- `README.md`: This file.

## How to Play

1. When you load the web page, you will see a button to load a random Dulux colour.
2. Click "Random Colour" to see the name and group of the colour.
3. Guess what this colour looks like!
4. Click "Show" to display the actual colour.

## Contributing

If you wish to contribute, you can create a pull request or send in suggestions to improve the game.

## Authors

- **Jesse Matthews** - _Initial work_

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
