import requests #It is a library which helps in fetching the data with the help of URL
import tkinter as tk
from tkinter import *
import customtkinter

def getWord(canvas):
    word=textfield.get()
    url = "https://wordsapiv1.p.rapidapi.com/words/"+word

    headers = {
        "X-RapidAPI-Key": "b350c1a455mshbf0aa23e684befcp1aed76jsn7f0d6b7bfb92",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }
    response= requests.get(url,headers=headers)
    json_data =response.json()
    if "results" in json_data:
        results = json_data["results"]
        
        if results:
            the_word = "\n" + word
            final_data = ""

            for i, result in enumerate(results[:3]):
                part_of_speech = result.get("partOfSpeech","Part of speech not found")
                definition = result.get("definition", "Definition not found")
                examples = result.get("examples", "Examples not found")
                synonyms=result.get("synonyms", "Synonyms not found")
                final_data += f"\n\n{i + 1}. {part_of_speech}\nDefinition: \n{definition}\n Examples: \n {examples}\n Synonyms: \n {synonyms}"

        else:
            final_data = "\nNo results found for: " + word
    else:
        final_data = "\nWord not found or no data available for: " + word

    
    l1.configure(text=the_word)
    l2.configure(text=final_data)
    

canvas = customtkinter.CTk()
canvas.title("Dictionary")
font1=("arial",20,"bold")
font2=("arial",15)
width = 700 #canvas width
height = 400 #canvas height
screen_width = canvas.winfo_screenwidth()  # Width of the screen
screen_height = canvas.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

canvas.geometry('%dx%d+%d+%d' % (width, width, x, y))
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
textfield = customtkinter.CTkEntry(master=canvas,font=font1,width=400,corner_radius=15)
textfield.pack(pady=20)
textfield.focus()#text remains focused
textfield.bind('<Return>',getWord)

#labels to show data
l1=customtkinter.CTkLabel(master=canvas,font=font1,text="")
l1.pack()

l2=customtkinter.CTkLabel(master=canvas,font=font2,text="") #text to hide the label until I click
l2.pack()


canvas.mainloop()
