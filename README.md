# 🎧 Binaural Beat Generator

A simple Python script that generates binaural beats to enhance focus, relaxation, or sleep by playing different frequencies in each ear.

## 📌 Features
- Customizable **base frequency** and **beat frequency**
- Set **duration in minutes**
- Ability to **stop playback early** with a keypress
- Uses **NumPy** for signal generation and **sounddevice** for playback

---

## 🚀 Installation

1. **Clone this repository** (or download the script directly):
   ```sh
   git clone https://github.com/jeffbalagosa/binaural-beat-generator.git
   cd binaural-beat-generator
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

---

## 🎵 Usage

### 🏃 Run the Script
```sh
python main.py
```

You'll be prompted to enter:
- **Base frequency** (default: 100 Hz)
- **Beat frequency** (default: 15 Hz)
- **Duration** in minutes (default: 25 minutes)

Or, you can run it with hardcoded defaults:
```sh
python main.py
```

### 🎧 Stopping Early
- You can stop playback anytime by pressing **Enter**.

---

## 🎯 Example Use Cases
| **Mode**        | **Base Frequency (Hz)** | **Beat Frequency (Hz)** | **Purpose** |
|---------------|------------------|------------------|---------|
| **Deep Focus**   | 140 Hz           | 18 Hz            | Intense concentration |
| **Light Focus**  | 120 Hz           | 14 Hz            | General productivity |
| **Creativity**   | 100 Hz           | 10 Hz            | Idea generation |
| **Relaxation**   | 90 Hz            | 7 Hz             | Stress relief |
| **Meditation**   | 80 Hz            | 6 Hz             | Deep relaxation |
| **Deep Sleep**   | 75 Hz            | 3 Hz             | Sleep induction |

---

## 🎶 How It Works
Binaural beats work by playing two slightly different frequencies in each ear.
Your brain perceives a third "phantom frequency," which influences brainwave activity:

- **Delta (1–4 Hz)** → Deep sleep
- **Theta (4–8 Hz)** → Meditation & relaxation
- **Alpha (8–13 Hz)** → Light focus & creativity
- **Beta (13–30 Hz)** → Alertness & problem-solving
- **Gamma (30+ Hz)** → High-level cognition

---

## 🛠 Dependencies
This project requires:
- **Python 3.8+**
- **NumPy** (`numpy`)
- **sounddevice** (`sounddevice`)
- **cffi** (`cffi`)
- **pycparser** (`pycparser`)

---

## 💡 Alternative Usage
If you don't want to run Python scripts, you can:
- Use **web-based binaural beat generators** like myNoise or Brain.fm.
- Convert the output to an **audio file** and play it on any device.

---

## 📚 License
MIT License

---

## ✨ Future Enhancements (Ideas)
- ✅ Add an **GUI version** (Tkinter or PyQt)
- ✅ Pre-configured **focus, sleep, and meditation modes**
- ✅ Allow **saving custom presets**

Enjoy your binaural beats! 🎧
