# -*- coding: utf-8 -*-
"""
Created on Sat May 12 18:55:35 2018

@author: Yggdrasil
"""
from tkinter import Label, Button, Frame, Tk
from random import randint
import copy


class App:

    questions = []

    question_number = 0

    old_questions = []

    right_answer = ""

    def read_file():

        filename = "./Fragen.txt"

        with open(filename) as csvfile:
            data = csvfile.readlines()
            for a in range(7, len(data)):
                App.questions.append(data[a].strip().split(","))

    def __init__(self, master):

        App.read_file()
        App.old_questions = copy.deepcopy(App.questions)
        frame = Frame(master, bg="SpringGreen3", width=200)
        frame.pack()

        # Schließen-Button: Closes the applet
        self.button = Button(frame,
                             text="Schließen",
                             fg="red",
                             command=frame.quit)
        self.button.grid(row=5, column=0, columnspan=2, pady=10)

        # Überschrifts-Label
        self.slogan = Label(frame,
                            text="Das Biophysik Quiz")
        self.slogan.grid(row=0, columnspan=2)

        # Nächste-Frage-Button: Writes the next question in the questions
        # and the answers in the fields
        self.next_quest = Button(frame,
                                 text="Nächste Frage",
                                 command=self.write_question)
        self.next_quest.grid(row=1,
                             columnspan=2,
                             pady=10,
                             padx=10)

        # Label-Field for the questions
        self.question_label = Label(frame,
                                    text="Hier stehen die Fragen",
                                    bg="CadetBlue2",
                                    wraplength=240)
        self.question_label.grid(row=2,
                                 column=0,
                                 columnspan=2,
                                 ipady=40,
                                 ipadx=60)

        # Answer-Button for the first answer
        self.first_ans = Button(frame,
                                text="erste Antwort",
                                bg="light sky blue",
                                command=lambda: self.check_answers(
                                        self.first_ans.config('text')[-1], 1))
        self.first_ans.grid(row=3,
                            column=0,
                            padx=5,
                            pady=5)

        # Answer-Button for the second answer
        self.sec_ans = Button(frame,
                              text="zweite Antwort",
                              bg="light sky blue",
                              command=lambda: self.check_answers(
                                      self.sec_ans.config('text')[-1], 2))
        self.sec_ans.grid(row=3,
                          column=1,
                          padx=5,
                          pady=5)

        # Answer-Button for the third answer
        self.third_ans = Button(frame,
                                text="dritte Antwort",
                                bg="light sky blue",
                                command=lambda: self.check_answers(
                                        self.third_ans.config('text')[-1], 3))
        self.third_ans.grid(row=4,
                            column=0,
                            padx=5,
                            pady=5)

        # Answer-Button for the fourth answer
        self.fourth_ans = Button(frame,
                                 text="vierte Antwort",
                                 bg="light sky blue",
                                 command=lambda: self.check_answers(
                                        self.fourth_ans.config('text')[-1], 4))
        self.fourth_ans.grid(row=4,
                             column=1,
                             padx=5,
                             pady=5)

    def write_question(self):

        self.first_ans.config(bg="light sky blue")
        self.sec_ans.config(bg="light sky blue")
        self.third_ans.config(bg="light sky blue")
        self.fourth_ans.config(bg="light sky blue")

        number = randint(0, len(App.questions)-1)
        App.question_number = number
        App.right_answer = App.questions[number][1]

        if(len(App.questions) != 0):

            frage = App.questions[number][0]

            self.question_label.config(text=frage)

            ans_place = list(range(1, 5))

            for i in range(4):
                place = randint(0, 3-i)

                if(i == 0):
                    self.first_ans.config(
                                text=App.questions[number][ans_place[place]])

                    ans_place.remove(ans_place[place])

                elif(i == 1):
                    self.sec_ans.config(
                                text=App.questions[number][ans_place[place]])

                    ans_place.remove(ans_place[place])

                elif(i == 2):
                    self.third_ans.config(
                                text=App.questions[number][ans_place[place]])

                    ans_place.remove(ans_place[place])

                else:
                    self.fourth_ans.config(
                                text=App.questions[number][ans_place[place]])

                    ans_place.remove(ans_place[place])

            App.questions.remove(App.questions[number])

        else:
            self.question_label.config(
                    text="Leider gibt es keine Fragen mehr :(")

    def check_answers(self, text, button_nr):

        if (text == App.right_answer):
            if(button_nr == 1):
                self.first_ans.config(bg="lawn green")
            if(button_nr == 2):
                self.sec_ans.config(bg="lawn green")
            if(button_nr == 3):
                self.third_ans.config(bg="lawn green")
            if(button_nr == 4):
                self.fourth_ans.config(bg="lawn green")
        else:
            if(button_nr == 1):
                self.first_ans.config(bg="orange red")
            if(button_nr == 2):
                self.sec_ans.config(bg="orange red")
            if(button_nr == 3):
                self.third_ans.config(bg="orange red")
            if(button_nr == 4):
                self.fourth_ans.config(bg="orange red")


root = Tk()
app = App(root)
root.mainloop()
