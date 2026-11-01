import os
import time
import sys
import warnings
from pathlib import Path


# ignore and remove pygame support texts
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
warnings.filterwarnings("ignore", category=RuntimeWarning, module="pygame")

try:
    import pygame
   
except ImportError:
    pygame = None
    print("Warning: pygame not installed. Audio disabled.")

# --- HARDCODED PATHS ---
QUOTES_FILE = Path.cwd() / "quotes" / "quotes.complete.txt"
MUSIC_FILE = Path.cwd() / "music.mp3"

CLEAR_SCREEN = "\033[2J\033[H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

class AudioPlayer:
    def __init__(self, file_path: Path):
        self.is_playing = False
        if not pygame:
            return
        if not file_path.exists():
            print(f"Audio file not found: {file_path}")
            return
        
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(str(file_path))
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1) # Loop forever
            self.is_playing = True
        except (pygame.error, OSError) as e:
            print(f"Failed to start audio: {e}")

    def stop(self) -> None:
        if self.is_playing and pygame:
            pygame.mixer.music.stop()


def animate_fade(text: str, fade_in: bool = True, speed: float = 0.03) -> None:
    if fade_in:
        color_range = range(232, 256, 3)  # Dark gray to white
    else:
        color_range = range(255, 231, -3) # White to dark gray

    for color in color_range:
        # \033[H goes to top-left. 
        # Because we clear the screen before fade_in, we don't need \033[J here.
        sys.stdout.write(f"\033[H\033[38;5;{color}m{text}\033[0m")
        sys.stdout.flush()
        time.sleep(speed)


def run_slideshow():
    if not QUOTES_FILE.exists():
        print(f"Error: Could not find {QUOTES_FILE}")
        return

    try:
        with open(QUOTES_FILE, "r", encoding="utf-8") as f:
            quotes = [line.strip() for line in f if line.strip()]
    except OSError as e:
        print(f"Error reading file: {e}")
        return

    if not quotes:
        print("The quotes file is empty!")
        return

    sys.stdout.write(CLEAR_SCREEN)
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.flush()
    
    time.sleep(1)

    try:
        for quote in quotes:
            # THE FIX: Completely clear the screen before the next quote fades in.
            # This wipes out any leftover text from a longer previous quote.
            sys.stdout.write("\033[H\033[J")
            sys.stdout.flush()
            
            animate_fade(quote, fade_in=True)
            time.sleep(3)
            animate_fade(quote, fade_in=False)
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        pass # Catch Ctrl+C cleanly
    finally:
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.write(CLEAR_SCREEN)
        sys.stdout.flush()
        print("\nSlideshow ended.")


if __name__ == "__main__":
    audio = AudioPlayer(MUSIC_FILE)
    try:
        run_slideshow()
    finally:
        audio.stop()


