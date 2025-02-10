import numpy as np
import sounddevice as sd
import threading
import argparse

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
    parser = argparse.ArgumentParser(description="Generate binaural beats")
    parser.add_argument(
        "--base",
        type=float,
        default=DEFAULT_BASE_FREQ,
        help=f"Base frequency in Hz (default: {DEFAULT_BASE_FREQ})",
    )
    parser.add_argument(
        "--beat",
        type=float,
        default=DEFAULT_BEAT_FREQ,
        help=f"Beat frequency in Hz (default: {DEFAULT_BEAT_FREQ})",
    )
    parser.add_argument(
        "--duration",
        type=float,
        default=DEFAULT_DURATION,
        help=f"Duration in minutes (default: {DEFAULT_DURATION})",
    )
    parser.add_argument(
        "--volume",
        type=float,
        default=DEFAULT_VOLUME,
        help=f"Volume from 0.0 to 1.0 (default: {DEFAULT_VOLUME})",
    )

    args = parser.parse_args()

    play_binaural_beat(
        base_freq=args.base,
        beat_freq=args.beat,
        duration=args.duration,
        volume=args.volume,
    )
