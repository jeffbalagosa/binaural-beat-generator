import numpy as np
import sounddevice as sd
import threading

# Configuration constants
DEFAULT_DURATION = 25  # minutes
DEFAULT_VOLUME = 0.1  # 0.0 to 1.0
DEFAULT_SAMPLE_RATE = 44100  # Hz


def play_brown_noise(
    duration=DEFAULT_DURATION,
    sample_rate=DEFAULT_SAMPLE_RATE,
    volume=DEFAULT_VOLUME,
):
    """
    Plays brown noise for a given duration.

    Parameters:
    - duration: Duration of the noise in minutes.
    - sample_rate: Audio sample rate.
    - volume: Volume scaling factor (0.0 to 1.0).
    """
    # Convert minutes to seconds
    duration_seconds = duration * 60
    n_samples = int(sample_rate * duration_seconds)

    # Generate white noise
    white_noise = np.random.randn(n_samples)

    # Generate brown noise by cumulatively summing the white noise
    brown_noise = np.cumsum(white_noise)

    # Normalize to prevent clipping (scale to -1.0 to 1.0)
    max_val = np.max(np.abs(brown_noise))
    if max_val != 0:
        brown_noise = brown_noise / max_val

    # Apply volume scaling
    brown_noise *= volume

    # Create a stereo signal (same signal on both channels)
    stereo_signal = np.column_stack((brown_noise, brown_noise))

    def play():
        print(f"Playing brown noise for {duration} minutes at volume {volume}.")
        sd.play(stereo_signal, samplerate=sample_rate)
        sd.wait()

    # Start playback in a separate thread so we can stop it early if needed.
    thread = threading.Thread(target=play)
    thread.start()

    input("\nPress Enter to stop playback early...\n")
    sd.stop()
    print("Playback stopped.")


if __name__ == "__main__":
    # Get user inputs for customization
    try:
        dur = float(input("Enter duration (minutes) [e.g., 25]: ") or DEFAULT_DURATION)
        volume = float(
            input("Enter volume (0.0 to 1.0) [e.g., 0.1]: ") or DEFAULT_VOLUME
        )
    except ValueError:
        print("Invalid input. Using default values.")
        dur, volume = DEFAULT_DURATION, DEFAULT_VOLUME

    play_brown_noise(duration=dur, volume=volume)
