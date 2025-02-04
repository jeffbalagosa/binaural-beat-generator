import numpy as np
import sounddevice as sd


def play_binaural_beat(
    base_freq=220, beat_freq=15, duration=10, sample_rate=44100, volume=0.5
):
    """
    Plays a binaural beat for a given duration.

    Parameters:
    - base_freq: The base frequency in Hz for the left ear.
    - beat_freq: The frequency difference between the ears (in Hz).
                The right ear tone will be (base_freq + beat_freq).
    - duration: Duration of the sound in seconds.
    - sample_rate: Audio sample rate.
    - volume: Volume scaling factor (0.0 to 1.0).
    """
    # Create a time array
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generate sine waves for both ears
    left_tone = np.sin(2 * np.pi * base_freq * t)
    right_tone = np.sin(2 * np.pi * (base_freq + beat_freq) * t)

    # Combine into a stereo signal: first column left, second column right
    stereo_signal = np.column_stack((left_tone, right_tone)) * volume

    # Play the stereo audio
    print(
        f"Playing binaural beats with {base_freq} Hz (left) and {base_freq + beat_freq} Hz (right) for {duration} seconds."
    )
    sd.play(stereo_signal, samplerate=sample_rate)
    sd.wait()  # Wait until playback is finished


if __name__ == "__main__":
    # Get user inputs for customization
    try:
        base = float(input("Enter base frequency (Hz) [e.g., 220]: ") or 220)
        beat = float(input("Enter beat frequency (Hz) [e.g., 15]: ") or 15)
        dur = float(input("Enter duration (seconds) [e.g., 10]: ") or 10)
    except ValueError:
        print("Invalid input. Using default values.")
        base, beat, dur = 220, 15, 10

    play_binaural_beat(base_freq=base, beat_freq=beat, duration=dur)
