# Album Art to ASCII
#### Video Demo:  <https://youtu.be/g9e8EpK2NFc>

**Album Art to ASCII** is a command-line application that lets users explore an artist’s discography and visualize album artwork as ASCII art directly in the terminal.

By connecting to the **iTunes Search API**, the program retrieves detailed album data — including names and cover images — and presents them in a clean, interactive interface.
After selecting an album, the program automatically downloads its cover, enhances its resolution, and converts the image into ASCII characters using pixel brightness mapping.

The result is a unique and lightweight way to experience music visually, without relying on graphical interfaces.



## Installation

Use the package manager pip to install Album Art to ASCII.

```bash
pip install -r requirements.txt
```

## Usage/Examples

You can run the script directly from the terminal:
```python
python project.py
```
Then, follow the on-screen prompts:
```python
Artist name: Rex Orange County
```
The program will:

    1. Fetch the artist’s albums from the iTunes API.
    2. Display the discography in a numbered list.
    3. Ask you to choose an album.
    4. Download and display the album artwork as ASCII art in the terminal.
Example output:

    1. Apricot Princess
    2. Pony
    3. Bcos U Will Never B Free
    4. WHO CARES?
    5. The Alexander Technique
    6. Live at Radio City Music Hall

    Pick an Album/EP (number): : 3
Result:

    [ASCII rendering of the album cover appears here]
## Features

- Search for artists using the iTunes API
- Display a full list of albums with cover art
- Convert album covers to ASCII art
- Adjustable ASCII resolution and scaling
- Lightweight and fully terminal-based


## Documentation

The project is organized into modular functions to handle different parts of the workflow — from fetching data via the iTunes API to rendering ASCII art in the terminal.

|                    Function                   |                                                           Description                                                                   |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `get_id(artist_name)`                         | Searches the iTunes API for the given artist name and returns the artist’s unique ID. Returns `None` if the artist is not found.        |
| `get_albums(artist_id)`                       | Retrieves the list of albums for a given artist ID from the iTunes API and returns a list of dictionaries containing album information. |
| `show_albums(discography)`                    | Displays the artist’s albums in a numbered list format. If no albums are found, the program exits with a message.                       |
| `choose_album(discography)`                   | Prompts the user to select an album by number and returns the corresponding artwork URL and album name.                                 |
| `increase_artwork_resolution(url, size=1000)` | Replaces the default low-resolution image URL with a higher resolution version (default: 1000×1000).                                    |
| `ascii_artwork(filename)`                     | Converts the downloaded album cover into ASCII art using brightness-based character mapping and prints it to the terminal.              |
| `cleanup(filename)`                           | Deletes temporary image files created during execution to keep the project folder clean.                                                |
| `main()`                                      | Coordinates the program flow — from artist search to displaying the ASCII artwork — by calling the functions above.                     |




## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Acknowledgements

This project was developed as part of CS50’s Introduction to Programming with Python.
Special thanks to the CS50 staff for providing the foundational materials and guidance that inspired the creation of this project.
The iTunes Search API was used to retrieve artist and album data.
The ASCII conversion functionality was made possible through the open-source ascii_magic and Pillow libraries.
- [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/)
- [ascii_magic](https://pypi.org/project/ascii-magic/)
- [Pillow](https://python-pillow.org/)

