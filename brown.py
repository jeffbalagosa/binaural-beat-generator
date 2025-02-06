import numpy as np
import sounddevice as sd

# Configuration Constants
DEFAULT_DURATION = 300  # seconds (5 minutes)
DEFAULT_SAMPLE_RATE = 44100  # Hz
DEFAULT_VOLUME = 0.5  # Volume (0.0 - 1.0)
VOLUME_MULTIPLIER = 4  # Amplification factor

def generate_brown_noise(
    duration=DEFAULT_DURATION, sample_rate=DEFAULT_SAMPLE_RATE, volume=DEFAULT_VOLUME, volume_multiplier=VOLUME_MULTIPLIER
):
    """
    Generates and plays Brown Noise.

    Parameters:
    - duration: Duration of playback in seconds.
    - sample_rate: Audio sample rate.
    - volume: Volume level (0.0 to 1.0).
    - volume_multiplier: Amplification factor for the volume.
    """
    num_samples = int(duration * sample_rate)

    # Generate Brownian motion (cumulative sum of random steps)
    brown_noise = np.cumsum(np.random.randn(num_samples))

    # Normalize to range [-1, 1] like the sine waves
    brown_noise = brown_noise / np.max(np.abs(brown_noise))

    # Scale volume
    brown_noise *= (volume * volume_multiplier)

    # Play the generated noise
    print(f"Playing Brown Noise for {duration} seconds...")
    sd.play(brown_noise, samplerate=sample_rate)
    sd.wait()


if __name__ == "__main__":
    try:
        dur = float(
            input("Enter duration (seconds) [default 300]: ") or DEFAULT_DURATION
        )
        vol = float(input("Enter volume (0.0 - 1.0) [default 0.5]: ") or DEFAULT_VOLUME)
    except ValueError:
        print("Invalid input. Using default values.")
        dur, vol = DEFAULT_DURATION, DEFAULT_VOLUME

    generate_brown_noise(duration=dur, volume=vol)
