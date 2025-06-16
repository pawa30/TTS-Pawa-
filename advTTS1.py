import pyttsx3
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

def speak():
    text = text_area.get("1.0", tk.END).strip()
    if text:
        engine.setProperty('rate', rate_slider.get())
        engine.setProperty('volume', volume_slider.get())
        selected_voice = voice_combobox.get()
        for voice in voices:
            if selected_voice in voice.name:
                engine.setProperty('voice', voice.id)
                break
        engine.say(text)
        engine.runAndWait()

def stop_speaking():
    engine.stop()

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Create GUI window
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("400x400")

# Text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(pady=10)

# Voice selection
voice_label = tk.Label(root, text="Select Voice:")
voice_label.pack()
voice_combobox = ttk.Combobox(root, values=[voice.name for voice in voices])
voice_combobox.set(voices[0].name)
voice_combobox.pack(pady=5)

# Rate slider
rate_label = tk.Label(root, text="Speech Rate:")
rate_label.pack()
rate_slider = tk.Scale(root, from_=50, to=300, orient=tk.HORIZONTAL)
rate_slider.set(150)
rate_slider.pack(pady=5)

# Volume slider
volume_label = tk.Label(root, text="Volume:")
volume_label.pack()
volume_slider = tk.Scale(root, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL)
volume_slider.set(1.0)
volume_slider.pack(pady=5)

# Buttons
speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_speaking)
stop_button.pack(pady=5)

# Run the GUI loop
root.mainloop()
