import whisper
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import pyaudio
import wave
import threading

model = whisper.load_model("medium")

is_recording = False
stream = None
frames = []

def record_audio(filename):
    global is_recording, stream, frames

    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 16000

    p = pyaudio.PyAudio()

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []
    is_recording = True
    status_label.config(text="System is recording...", fg="green")

    while is_recording:
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    status_label.config(text="Recording finished.", fg="blue")
    print("Recording finished.")

def stop_recording():
    global is_recording
    is_recording = False
    status_label.config(text="Recording stopped.", fg="red")

def transcribe_audio():
    audio_file = "temp_recording.wav"
    record_audio(audio_file)

    status_label.config(text="Processing transcription...", fg="orange")
    root.update()

    result = model.transcribe(audio_file)
    transcription = result["text"]

    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, transcription)

    status_label.config(text="Transcription complete.", fg="green")

def export_transcription():
    transcription = text_box.get(1.0, tk.END).strip()

    if not transcription:
        messagebox.showwarning("Warning", "No transcription to export!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        title="Save Transcription As"
    )

    if file_path:
        try:
            with open(file_path, "w") as f:
                f.write(transcription)
            messagebox.showinfo("Success", f"Transcription saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

def start_transcription():
    if is_recording:
        messagebox.showwarning("Warning", "Recording is already in progress!")
        return
    threading.Thread(target=transcribe_audio).start()

root = tk.Tk()
root.title("Live Captioning with Whisper")

mic_button = tk.Button(root, text="🎤 Start Recording", command=start_transcription)
mic_button.pack(pady=10)

stop_button = tk.Button(root, text="⏹ Stop Recording", command=stop_recording)
stop_button.pack(pady=10)

export_button = tk.Button(root, text="💾 Export Transcription", command=export_transcription)
export_button.pack(pady=10)

status_label = tk.Label(root, text="System is not recording.", fg="black")
status_label.pack(pady=10)

text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
text_box.pack(pady=10)

root.mainloop()
