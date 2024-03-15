import tkinter as tk
import pyttsx3

from googletrans import Translator
class LangTranslator():
    def lang_translator(self,lang):
        user_input=textarea.get(0.0,tk.END)
        translator=Translator()
        self.result=translator.translate(user_input,dest=lang)
        output.config(text=self.result.text)

    def speak(self):
        if self.result.dest=='en':
            pyttsx3.speak(self.result.text)
        else:
            output.config(text="Sorry! Can't speak this language")

lt=LangTranslator()



root=tk.Tk()
root.title('Google Translator')
root.geometry("950x700")

translate_btn=tk.Button(text="Translate",font=("Bahnschrift",25),width=10,relief="solid",bg="#008744",command=lambda:lt.lang_translator('en'))
speak_btn=tk.Button(text="Speak",font=("Bahnschrift",25),width=10,relief="solid",bg="#ffa700",command=lt.speak)
hindi_btn=tk.Button(text="Hindi",font=("Bahnschrift",25),width=10,relief="solid",bg="#0057e7",command=lambda:lt.lang_translator('hi'))
punjabi_btn=tk.Button(text="Punjabi",font=("Bahnschrift",25),width=10,relief="solid",bg="#d62d20",command=lambda:lt.lang_translator('punjabi'))

translate_btn.grid(row=1,column=1,pady=5,padx=10)
speak_btn.grid(row=2,column=1,pady=5,padx=10)
hindi_btn.grid(row=3,column=1,pady=5,padx=10)
punjabi_btn.grid(row=4,column=1,pady=5,padx=10)


textarea=tk.Text(relief='solid',font=("Arial",13),height=20)
textarea.grid(row=1,column=2,rowspan=4)

sub_heading=tk.Label(text="Translation",font=("Impact",25),fg='#4a80f5')
sub_heading.grid(row=5,column=1,columnspan=2,pady=10)

output=tk.Label(text="",font=("Arial",25),bg='white')
output.grid(row=6,column=1,columnspan=2,pady=10)


root.mainloop()
