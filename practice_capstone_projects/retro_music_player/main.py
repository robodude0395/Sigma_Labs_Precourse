import pygame
import numpy as np
import librosa
import time

# --- SETTINGS ---
AUDIO_FILE = "song.mp3"
FPS = 24
NUM_BARS = 60
WIDTH, HEIGHT = 800, 400

# --- LOAD AUDIO (for FFT only, not playback) ---
print("Loading audio for visualization...")

"""
y: a 1D NumPy array of floating-point audio samples. Values are normalized between -1 and 1.

sr: the sample rate, i.e., how many samples per second (e.g., 22050 Hz by default).
"""
y, sr = librosa.load(AUDIO_FILE, mono=True)
print(f"Loaded {len(y)} samples at {sr} Hz")

# Normalize
y = y / np.max(np.abs(y))

# --- PYGAME SETUP ---
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro FFT Visualizer (pygame only)")
clock = pygame.time.Clock()

# --- PLAYBACK ---
pygame.mixer.music.load(AUDIO_FILE)
pygame.mixer.music.play()

# --- VISUALIZATION SETTINGS ---
chunk_size = int(sr / FPS)
bar_width = WIDTH // NUM_BARS

start_time = time.time()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    elapsed = time.time() - start_time
    pos = int(elapsed * sr)
    if pos + chunk_size >= len(y):
        running = False
        break

    # Get chunk and compute FFT
    chunk = y[pos:pos + chunk_size]
    if len(chunk) == 0:
        continue

    fft = np.abs(np.fft.rfft(chunk))
    fft = np.log1p(fft)
    fft = fft[:NUM_BARS * 2]

    #Splits the FFT bins evenly into NUM_BARS groups.
    bars = np.mean(fft.reshape(NUM_BARS, -1), axis=1)

    max_val = np.max(bars)
    if max_val > 0 and not np.isnan(max_val):
        bars = bars / max_val * HEIGHT
    else:
        bars = np.zeros_like(bars)

    screen.fill((10, 10, 30))
    for i, val in enumerate(bars):
        val = max(0, min(HEIGHT, int(val)))
        x = i * bar_width
        y_pos = HEIGHT - val
        color = (0, 255 - int(val / HEIGHT * 255), 120)
        pygame.draw.rect(screen, color, (int(x), int(y_pos), int(bar_width - 2), int(val)))

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()