import numpy as np
import sounddevice as sd
import threading

# Configuration constants
DEFAULT_BASE_FREQ = 100  # Hz
DEFAULT_BEAT_FREQ = 15  # Hz
DEFAULT_DURATION = 25  # minutes
DEFAULT_VOLUME = 0.1  # 0.0 to 1.0


def play_binaural_beat(
    base_freq=DEFAULT_BASE_FREQ,
    beat_freq=DEFAULT_BEAT_FREQ,
    duration=DEFAULT_DURATION,
    sample_rate=44100,
    volume=DEFAULT_VOLUME,
):
    """
    Plays a binaural beat for a given duration.

    Parameters:
    - base_freq: The base frequency in Hz for the left ear.
    - beat_freq: The frequency difference between the ears (in Hz).
    - duration: Duration of the sound in minutes.
    - sample_rate: Audio sample rate.
    - volume: Volume scaling factor (0.0 to 1.0).
    """
    # Convert minutes to seconds
    duration_seconds = duration * 60

    # Create a time array
    t = np.linspace(
        0, duration_seconds, int(sample_rate * duration_seconds), endpoint=False
    )

    # Generate sine waves for both ears
    left_tone = np.sin(2 * np.pi * base_freq * t)
    right_tone = np.sin(2 * np.pi * (base_freq + beat_freq) * t)

    # Combine into a stereo signal: first column left, second column right
    stereo_signal = np.column_stack((left_tone, right_tone)) * volume

    # Play the stereo audio in a separate thread so we can stop it
    def play():
        print(
            f"Playing binaural beats with {base_freq} Hz (left) and {base_freq + beat_freq} Hz (right) for {duration} minutes at volume {volume}."
        )
        sd.play(stereo_signal, samplerate=sample_rate)
        sd.wait()

    thread = threading.Thread(target=play)
    thread.start()

    # Allow the user to stop playback manually
    input("\nPress Enter to stop playback early...\n")
    sd.stop()
    print("Playback stopped.")


if __name__ == "__main__":
    # Get user inputs for customization
    try:
        base = float(
            input("Enter base frequency (Hz) [e.g., 100]: ") or DEFAULT_BASE_FREQ
        )
        beat = float(
            input("Enter beat frequency (Hz) [e.g., 15]: ") or DEFAULT_BEAT_FREQ
        )
        dur = float(input("Enter duration (minutes) [e.g., 25]: ") or DEFAULT_DURATION)
        volume = float(
            input("Enter volume (0.0 to 1.0) [e.g., 0.1]: ") or DEFAULT_VOLUME
        )
    except ValueError:
        print("Invalid input. Using default values.")
        base, beat, dur, volume = (
            DEFAULT_BASE_FREQ,
            DEFAULT_BEAT_FREQ,
            DEFAULT_DURATION,
            DEFAULT_VOLUME,
        )

    play_binaural_beat(base_freq=base, beat_freq=beat, duration=dur, volume=volume)
