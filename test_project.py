import pytest
import tempfile, os
from project import show_albums, increase_artwork_resolution, choose_album, cleanup

def test_choose_album(monkeypatch):
    discography = [
        {"number": 1, "name": "Album A", "artwork": "urlA"},
        {"number": 2, "name": "Album B", "artwork": "urlB"},
    ]
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert choose_album(discography) == ("urlB", "Album B")

def test_choose_album_invalid(monkeypatch):
    discography = [{"number": 1, "name": "Album A", "artwork": "urlA"}]
    monkeypatch.setattr('builtins.input', lambda _: "9")
    assert choose_album(discography) == (None, None)

def test_show_albums_empty():
    with pytest.raises(SystemExit) as e:
        show_albums(None)
    assert str(e.value) == "This artist does not have albums available."

def test_show_albums_print(capsys):
    discography = [
        {"number": 1, "name": "Salad Days", "artwork": "url"},
        {"number": 2, "name": "2", "artwork": "url"}
    ]
    show_albums(discography)
    captured = capsys.readouterr()
    assert "1. Salad Days" in captured.out
    assert "2. 2" in captured.out

def test_increase_artwork_resolution():
    url = "https://is5-ssl.mzstatic.com/image/thumb/Music122/v4/ab/cd/ef/abcdef123456/100x100bb.jpg"
    expected = "https://is5-ssl.mzstatic.com/image/thumb/Music122/v4/ab/cd/ef/abcdef123456/1000x1000bb.jpg"
    assert increase_artwork_resolution(url) == expected

    expected_500 = url.replace("100x100bb", "500x500bb")
    assert increase_artwork_resolution(url, size=500) == expected_500

    assert increase_artwork_resolution(None) is None

def test_cleanup():
    temp = tempfile.NamedTemporaryFile(delete=False)
    name = temp.name
    temp.close()
    cleanup(name)
    assert not os.path.exists(name)
