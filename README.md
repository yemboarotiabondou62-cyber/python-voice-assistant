# Python Voice Assistant 🎙️

A lightweight, interactive voice assistant built with Python and a modern GUI. It listens to natural language commands and automates tasks like searching and playing YouTube videos.

## ✨ Key Features
* **Modern GUI:** Clean and simple interface built with `customtkinter`.
* **Voice & TTS:** Real-time speech recognition and text-to-speech feedback (`SpeechRecognition`, `pyttsx3`).
* **YouTube Integration:** Say *"joue [song]"* to automatically search and launch the video in your default browser.
* **Robust Processing:** Auto-formats commands for reliable execution.

## 🛠️ Requirements
Recommended: **Python 3.11 or 3.12**.

**Dependencies:**
`customtkinter`, `SpeechRecognition`, `PyAudio`, `youtube-search`, `pyttsx3`

*⚠️ **Important Note:** You must install `comtypes==1.1.14` to prevent fatal Python crashes when running `pyttsx3` alongside a GUI on newer Python versions.*

## 🚀 Quick Start

1. **Setup your environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
