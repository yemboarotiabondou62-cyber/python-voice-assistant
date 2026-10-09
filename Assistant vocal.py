from re import search

import customtkinter as ctk
import speech_recognition as sr
import pyttsx3
from youtube_search import YoutubeSearch
import webbrowser


#initialiser la synthes vocale et la reconnaisance vocale

recognizer = sr.Recognizer()
engine = pyttsx3.init()

#fonction pour parler(synthese vocale)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#fonction pour ecouter et reconnaitre la voie

def recognizer_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Parlez maintenant")

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language="fr-FR")
            print(f"Vous avez dit {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Je n'ai pas compris")
            return ""
        except sr.RequestError as e:
            print("Erreur de connexion")
            return ""


#fonction pour executer les commandes vocales
def execute_command():
    command = recognizer_speech()

    if "joue" in command:
        song_name = command.replace("Joue", "").strip()
        speak(f"Recherche de {song_name} sur Youtube")
         #recherche sur youtube


        result = YoutubeSearch(song_name,max_results = 1).to_dict()
        if result:
            video_url = f"https://www.youtube.com/watch?v={result[0]["id"]}"
            speak(f"lecture de {result[0]["title"]}.")
            webbrowser.open(video_url)

        else:
            print("Aucune video trouver")

    elif "Ouvre Youtube" in command:
        speak("Ouverture de Youtube")
        webbrowser.open(f"https://www.youtube.com/")

    elif "ferme" in command:
        print("fermeture de l'application")
        app.quit()
    else:
        speak("Command non reconnue")

















#Initialiser l'application

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("500x400")
app.title("Assistant Vocal")

#Label d'instruction

label = ctk.CTkLabel(app,text = "Cliquer sur le boutton pour ecouter une commande",font = ("helvetica",16))
label.pack(pady = 30)

#boutton pour ecouter la commande

ecoute_boutton = ctk.CTkButton(app,text = "Ecouter",command = execute_command,font = ("helvetica",14),height=50,width = 200)
ecoute_boutton.pack(pady = 20)

#boutton pour ecouter la commande

quitter_boutton = ctk.CTkButton(app,text = "Quitter",command = app.quit(),font = ("helvetica",14),height=50,width = 200,fg_color="red")
quitter_boutton.pack(pady = 20)





app.mainloop()
