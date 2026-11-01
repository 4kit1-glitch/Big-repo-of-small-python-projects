# slide show program 
# run scrollS.py first before run
# or conplete jsS.py and run 


import time
import sys
import os
import pygame
from pathlib import Path

# --- CONFIGURATION ---
QUOTES_FILE = Path.cwd() / "quotes" / "quotes.complete.txt" 
MUSIC_FILE = Path.cwd() / "music.mp3"
FADE_SPEED = 0.03  
DISPLAY_TIME = 4  

MUSIC_VOLUME = 0.3

def play_music(file_path) -> bool:
    if not file_path.exists():
        print("No music file found. Running silently.")
        return False
        
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(str(file_path))
        pygame.mixer.music.set_volume(MUSIC_VOLUME) 
        pygame.mixer.music.play(-1) # -1 means loop forever
        return True
    except OSError as e:
        print(f"Could not play music: {e}")
        return False

def print_fading(text, fade_in=True):
    # ANSI 256-color codes. 232 is almost black, 255 is pure white.
    if fade_in:
        color_range = range(232, 256, 2) # Dark to light
    else:
        color_range = range(255, 231, -2) # Light to dark

    for color in color_range:
        # \033[38;5;{color}m sets the text color
        sys.stdout.write(f"\033[38;5;{color}m{text}\033[0m\r")
        sys.stdout.flush()
        time.sleep(FADE_SPEED)

def start_slideshow(file_path):
    if not file_path.exists():
        print(f"Error: Could not find {file_path}")
        return

    # Load quotes
    with open(file_path, "r", encoding="utf-8") as f:
        quotes = [line.strip() for line in f if line.strip()]

    if not quotes:
        print("The quotes file is empty!")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Starting slideshow... (Press Ctrl+C to exit)\n")
    time.sleep(2)

    try:
        for quote in quotes:
            # Clear screen for the next quote
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Add some padding so it looks centered
            display_text = f"\n\n\n          {quote}"
            
            # Fade in
            print_fading(display_text, fade_in=True)
            
            # Keep it on screen
            time.sleep(DISPLAY_TIME)
            
            # Fade out
            print_fading(display_text, fade_in=False)
            
            time.sleep(0.5) # Small pause before the next quote
            
    except KeyboardInterrupt:
        pass # Catch Ctrl+C cleanly
    finally:
        pygame.mixer.music.stop()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nSlideshow ended.")

if __name__ == "__main__":
    # Make sure your paths are correct before running!
    has_music = play_music(MUSIC_FILE)
    
    start_slideshow(QUOTES_FILE)