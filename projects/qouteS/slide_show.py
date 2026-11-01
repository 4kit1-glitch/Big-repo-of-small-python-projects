# slide show program 
# run scrollS.py first before run
# or conplete jsS.py and run 

import argparse
import shutil
import sys
import time
from pathlib import Path

try:
    import pygame
except ImportError:
    print("Warning: pygame is not installed. Audio will be disabled.")
    pygame = None

# --- ANSI Escape Codes for Terminal Control ---
CLEAR_SCREEN = "\033[2J\033[H"
RESET_COLOR = "\033[0m"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"


# --- VOL CONTROL CODES ---
PLAY_VOLUME = 0.3

class AudioPlayer:
    def __init__(self, file_path: Path | None) -> None:
        self.is_playing = False
        if not file_path or not file_path.exists() or not pygame:
            return
        
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(str(file_path))
            pygame.mixer.music.set_volume(PLAY_VOLUME)
            pygame.mixer.music.play(-1)
            self.is_playing = True
        except (OSError, ValueError, TypeError) as e:
            print(f"Failed to start audio: {e}")

    def stop(self) -> None:
        if self.is_playing and pygame:
            pygame.mixer.music.stop()


def center_text(text: str) -> str:
    """Dynamically centers text based on the current terminal width."""
    terminal_width = shutil.get_terminal_size().columns
    # If the quote is longer than the terminal, just strip and return
    if len(text) >= terminal_width:
        return text.strip()
    
    padding = (terminal_width - len(text)) // 2
    return " " * padding + text.strip()


def animate_fade(text: str, fade_in: bool = True, speed: float = 0.02) -> None:
    """Animates a color fade from black to white (or vice versa)."""
    if fade_in:
        color_range = range(232, 256, 2)
    else:
        color_range = range(255, 231, -2)

    for color in color_range:
        # \r moves cursor to start, \033[K clears the line to prevent leftover text
        sys.stdout.write(f"\033[38;5;{color}m{text}\r\033[K")
        sys.stdout.flush()
        time.sleep(speed)


def run_slideshow(quotes_file: Path, duration: int, audio: AudioPlayer) -> None:
    try:
        with quotes_file.open("r", encoding="utf-8") as f:
            quotes = [line.strip() for line in f if line.strip()]
    except OSError as e:
        print(f"Error reading file {quotes_file}: {e}")
        return

    if not quotes:
        print("File is empty.")
        return

    print(HIDE_CURSOR, end="")
    print(CLEAR_SCREEN, end="")
    
    try:
        for quote in quotes:
            print(CLEAR_SCREEN, end="")
            
            # Center the text vertically (approx) and horizontally
            formatted_quote = center_text(quote)
            display_text = f"\n\n\n{formatted_quote}\n\n"
            
            animate_fade(display_text, fade_in=True)
            time.sleep(duration)
            animate_fade(display_text, fade_in=False)
            
            time.sleep(0.3) # Small pause before next quote
            
    except KeyboardInterrupt:
        pass # Graceful exit on Ctrl+C
    finally:
        print(SHOW_CURSOR, end="")
        print(CLEAR_SCREEN, end="")
        audio.stop()
        print("Slideshow ended.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Terminal Quote Slideshow")
    parser.add_argument("file", type=Path, help="Path to the quotes text file")
    parser.add_argument("--music", type=Path, help="Path to an mp3 file (optional)", default=None)
    parser.add_argument("--duration", type=int, default=4, help="Time to display each quote in seconds")
    parser.add_argument("--speed", type=float, default=0.02, help="Fade speed (lower is faster)")
    
    args = parser.parse_args()

    audio = AudioPlayer(args.music)
    
    run_slideshow(
        quotes_file=args.file,
        duration=args.duration,
        audio=audio
    )

if __name__ == "__main__":
    main()