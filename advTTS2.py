import pyttsx3
import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import ttk
from googletrans import Translator

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to change voice
def change_voice():
    voice = voice_combobox.get()
    voices = engine.getProperty('voices')
    for v in voices:
        if v.name == voice:
            engine.setProperty('voice', v.id)

# Function to speak the entered text
def speak():
    text = text_area.get("1.0", tk.END).strip()
    if text:
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showwarning("Input Error", "Please enter some text to speak.")

# Function to translate text
def translate_text():
    text = text_area.get("1.0", tk.END).strip()
    target_lang = language_combobox.get()
    if text:
        try:
            translator = Translator()
            translated = translator.translate(text, dest=target_lang)
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, translated.text)
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))
    else:
        messagebox.showwarning("Input Error", "Please enter some text to translate.")

# Create GUI window
root = tk.Tk()
root.title("Text to Speech Converter")
root.geometry("500x400")

# Label for text area
label = tk.Label(root, text="Enter text here:")
label.pack(pady=5)

# Text area for input
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=8)
text_area.pack(pady=10)

# Button to speak text
speak_button = tk.Button(root, text="Speak", command=speak)
speak_button.pack(pady=5)

# ComboBox for selecting voice
voices = engine.getProperty('voices')
voice_names = [v.name for v in voices]
voice_combobox = ttk.Combobox(root, values=voice_names, state="readonly")
voice_combobox.set(voice_names[0])  # Default voice
voice_combobox.pack(pady=5)

# Button to change voice
change_voice_button = tk.Button(root, text="Change Voice", command=change_voice)
change_voice_button.pack(pady=5)

# ComboBox for language selection (Translate)
languages = ["english", "es", "fr", "de", "it", "pt", "ru", "zh-cn"]
language_combobox = ttk.Combobox(root, values=languages, state="readonly")
language_combobox.set("english")  # Default to English
language_combobox.pack(pady=5)

# Button to translate text
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
