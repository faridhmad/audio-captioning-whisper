# Audio Captioning with Whisper

This project is a **real-time audio captioning tool** that uses OpenAI's Whisper model to transcribe audio from your microphone. It provides a simple graphical user interface (GUI) for recording audio, transcribing it, and exporting the transcription as a `.txt` file.

---

## Features

- **Real-Time Recording**: Record audio directly from your microphone.
- **Transcription**: Transcribe recorded audio using OpenAI's Whisper model.
- **Export Transcription**: Save the transcription as a `.txt` file.
- **User-Friendly Interface**: Built with `tkinter` for ease of use.
- **Cross-Platform**: Works on macOS, Windows, and Linux.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.7 or higher**
- **pip** (Python package manager)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/faridhmad/audio-captioning-whisper.git
   cd audio-captioning-whisper
   ```

2. **Install Required Libraries**:
   Run the following command to install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download Whisper Models**:
   The first time you run the script, it will download the Whisper model (`medium` by default). Ensure you have a stable internet connection.

---

## Usage

1. **Run the Script**:
   ```bash
   python whisper_transcription.py
   ```

2. **Using the GUI**:
   - **🎤 Start Recording**: Click to start recording audio.
   - **⏹ Stop Recording**: Click to stop recording and start transcription.
   - **💾 Export Transcription**: Click to save the transcription as a `.txt` file.

---

## Project Structure

```
audio-captioning-whisper/
├── whisper_transcription.py       # Main script for the transcription tool
├── requirements.txt               # List of required Python libraries
├── README.md                      # Project documentation
└── temp_recording.wav             # Temporary audio file (created during runtime)
```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **OpenAI Whisper**: For providing the powerful speech-to-text model.
- **PyAudio**: For enabling audio recording.
- **Tkinter**: For the simple and effective GUI.

---

```
