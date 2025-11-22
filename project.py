import requests
import sys
import os
from ascii_magic import AsciiArt
from PIL import Image


def main():
    while True:
        artist = get_name()
        artist_id = get_id(artist)
        if not artist_id:
            print("Artist not found. Try again.")
        else:
            break

    while True:
        discography = get_albums(artist_id)
        show_albums(discography)
        artwork_url, album_name = choose_album(discography)
        if not artwork_url:
            print("Album not found. Enter a valid number:")
        else:
            filename = get_artwork(artwork_url, album_name)
            ascii_artwork(filename)
            cleanup(filename)
            break

def get_name():
    return input("Artist name: ").lower().strip()

def get_id(artist):
    id_search = requests.get(f"https://itunes.apple.com/search?term={artist}&entity=musicArtist").json()
    if id_search["resultCount"] == 0:
        return None
    return id_search["results"][0]["artistId"]

def get_albums(artist_id):
    albums_data = requests.get(f"https://itunes.apple.com/lookup?id={artist_id}&entity=album").json()

    discography = []
    count = 1
    for result in albums_data["results"]:
        if result.get("collectionType") == "Album" and "single" not in result.get("collectionName").lower():
            discography.append({
                "number": count,
                "name": result["collectionName"],
                "artwork": increase_artwork_resolution(result["artworkUrl100"])
            })
            count += 1
    return discography

def show_albums(discography):
    if not discography:
        sys.exit("This artist does not have albums available.")
    for album in discography:
        print(f"{album['number']}. {album['name']}")

def choose_album(discography):
    album_pick = input("\nPick an Album/EP (number): ").strip()
    for album in discography:
        if album_pick == str(album["number"]):
            return album["artwork"], album["name"]
    return None, None

def increase_artwork_resolution(url, size=1000):
    if url:
        return url.replace("100x100bb", f"{size}x{size}bb")
    return url

def get_artwork(url, album_name="artwork"):
    img_data = requests.get(url).content
    filename = f"{album_name}.jpg"
    with open(filename, "wb") as handler:
        handler.write(img_data)
    return filename

def ascii_artwork(filename):
    img = Image.open(filename)
    my_art = AsciiArt.from_pillow_image(img)
    my_art.to_terminal(columns=180)

def cleanup(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass



if __name__ == "__main__":
    main()
