import webbrowser

# Dictionary to map song names to YouTube links
song_links = {
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "believer": "https://youtu.be/W0DM5lcj6mw?si=hrqoA5sF6H8A730d",
    "perfect": "https://youtu.be/cNGjD0VG4R8?si=Dl7urnamYvO0ouyb",
    "peaky blinders": "https://youtu.be/y7T3ax7JPwI?si=0xL9Zz-_o08bkzmY",
    # Add more songs here
}

def play(song_name):
    try:
        song_name = song_name.lower()  # normalize for matching
        if song_name in song_links:
            link = song_links[song_name]
            print(f"🎵 Playing '{song_name}': {link}")
            webbrowser.open(link)
            return True
        else:
            print(f"❌ Song '{song_name}' not found in playlist.")
            return False
    except Exception as e:
        print("Failed to play song:", e)
        return False
