#!/usr/bin/python3

#import required modules
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator
from textblob import TextBlob

# Create the main window
window = Tk()
window.title("J-J-Language Translator")
window.minsize(600, 500)
window.maxsize(600, 500)
window.configure(bg="#008080")  # Set background color


# Translation function
def translate():
    try:
        # Get input text and selected languages
        txt = text1.get(1.0, END)
        c1 = combo1.get()
        c2 = combo2.get()

        if txt:
<<<<<<< HEAD
            translator = Translator(service_urls=['translate.google.com'], timeout=5, api_key='2054495c77mshb9caf1e825426dep146d9fjsne91745bbddc3')
=======
            # Create a translator instance
            translator = Translator(service_urls=['translate.google.com'])

            # Translate the text
>>>>>>> fb4506a17db55e15144dc17c3308a0a3fca4e5ac
            result = translator.translate(txt, src=c1, dest=c2)
            translated_text = result.text

            # Display the translated text
            text2.delete(1.0, END)
            text2.insert(END, translated_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Get available languages
language = LANGUAGES
lang_value = list(language.values())
lang1 = language.keys()

# Create and configure the language selection dropdowns
combo1 = ttk.Combobox(window, values=lang_value, state='readonly')
combo1.place(x=100, y=20)
combo1.set("choose a language")

combo2 = ttk.Combobox(window, values=lang_value, state='readonly')
combo2.place(x=300, y=20)
combo2.set("choose a language")

# Create input and output text areas
f1 = Frame(window, bg='black', bd=4)
f1.place(x=100, y=100, width=150, height=150)

text1 = Text(f1, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=140, height=140)

f2 = Frame(window, bg='black', bd=4)
f2.place(x=300, y=100, width=150, height=150)

text2 = Text(f2, font="Roboto 14", bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=140, height=140)

# Create the translate button
button = Button(window, text='Translate', font=('normal', 15), bg='yellow', command=translate)
button.place(x=230, y=300)

# Start the main event loop
window.mainloop()
