import time
from tkinter import *


class Tamagotchi:
    """Skapar en Tamagotchi med inläst storlek och färg"""
    def __init__(self, rot, colour, size, ordning, save_time, good_outcomes):
        self.max_red = 110  # största storleken Tamagotchin kan bli
        self.min_red = 0  # minsta storleken Tamagotchin kan bli
        self.size_red = 1  # storleken Tamagotchin minskar eller ökar med åt gången
        self.rot = rot
        self.ordning = self.inlast_ordning(ordning)
        rot.geometry("372x450")
        self.size = int(size)
        self.colour = colour
        self.time_alone = self.time_alone(save_time)
        self.good_outcomes = good_outcomes
        self.canvas = Canvas(self.rot, width=372, height=279, bg="#fff")
        self.canvas.place(x=0, y=0)
        self.circle = self.canvas.create_oval(76, 30, 296, 250, fill=self.colour, outline="white", width=self.size)
        self.counter = 0
        self.titel = Label(self.rot, text="Teknologtamagotchin", height=1, width=47, background="white",
                           font="Helvetica 10 bold")
        self.titel.place(x=0, y=0)
        self.textruta = Label(self.rot, text="Du har lämnat mig ensam i " + self.time_alone,
                              height=1, width=62, background="white", font="Arial 8")
        self.textruta.place(x=0, y=259)
        self.knapp1 = Button(self.rot, text='Sova', width=25, height=5, command=lambda: self.knapptryck(1))
        self.knapp1.place(x=1, y=279)
        self.knapp2 = Button(self.rot, text='Plugga', width=25, height=5, command=lambda: self.knapptryck(2))
        self.knapp2.place(x=187, y=279)
        self.knapp3 = Button(self.rot, text='Tenta', width=25, height=5, command=lambda: self.knapptryck(3))
        self.knapp3.place(x=1, y=364)
        self.knapp4 = Button(self.rot, text='Festa', width=25, height=5, command=lambda: self.knapptryck(4))
        self.knapp4.place(x=187, y=364)
        self.rot.after(10000, self.shrink)  # Om ingen knapp trycks minskar storleken automatiskt

    def inlast_ordning(self, ordning):
        """Funktion som läser in ordningen av de tre senaste knapptryck som gjordes när programmet senast användes
        och returnerar ordningen"""
        order = []
        for i in ordning:
            number = int(i)
            order.append(number)
        return order

    def time_alone(self, save_time):
        """Funktion som räknar ut hur många dagar, timmar, minuter och sekunder
        som gått sedan programmet senast öppnades och returnerar detta"""
        flt_save = float(save_time)
        time_now = time.time()
        passed = round(time_now - flt_save)
        day = passed // (24 * 3600)
        rem_time = passed % (24 * 3600)
        hour = rem_time // 3600
        rem_time %= 3600
        minutes = rem_time // 60
        rem_time %= 60
        seconds = rem_time
        passed_str = str(day) + " dagar " + str(hour) + " timmar " + str(minutes) + " minuter och " + \
                     str(seconds) + " sekunder."
        return passed_str

    def knapptryck(self, i):
        """Funktion som lägger de knapptryck som gjorts i en lista och utvärderar dessa"""
        self.counter = 1
        self.ordning.append(i)
        if len(self.ordning) > 3:
            self.ordning.pop(0)
        if len(self.ordning) == 3 and self.ordning in self.good_outcomes:
            self.new_size(2)
            self.textruta.config(text="Det var en bra kombination! Min storlek är nu: " + str(110 - self.size))
        elif len(self.ordning) == 3:
            self.new_size(1)
            self.textruta.config(text="Det var en dålig kombination. Min storlek är nu: " + str(110 - self.size))

    def new_colour(self, new_colour):
        """Ändrar färgen på Tamagotchin"""
        if new_colour == 1:
            self.colour = "#000000"
        elif new_colour == 2:
            self.colour = "#0000FF"
        elif new_colour == 3:
            self.colour = "#FF00FF"
        self.canvas.itemconfig(self.circle, fill=self.colour)

    def new_size(self, new_size):
        """Ändrar storleken på Tamagotchin"""
        if new_size == 1 and self.size <= self.max_red:
            self.size += self.size_red
            self.canvas.itemconfig(self.circle, width=self.size)
            if self.size > 80:
                self.new_colour(1)
            elif 80 >= self.size > 30:
                self.new_colour(2)
        elif new_size == 2 and self.size > self.min_red:
            self.size -= self.size_red
            self.canvas.itemconfig(self.circle, width=self.size)
            if 80 >= self.size > 30:
                self.new_colour(2)
            elif self.size <= 30:
                self.new_colour(3)

    def shrink(self):
        """Ändrar storleken på Tamagotchin ju längre tiden går utan knapptryck"""
        if self.counter == 0:
            self.new_size(1)
            self.rot.after(3000, self.shrink)
        else:
            pass


class Data:
    """Läser in och sparar data om Tamagotchin"""
    def __init__(self):
        self.programdata = []
        self.order = []

    def inlas(self, textfile):
        """"Funktion som läser in färg och storlek från en fil och lägger till dessa i en lista som returneras"""
        with open(textfile, encoding='utf8') as file:
            raw_string = file.read()
            self.programdata = raw_string.split(sep="\n")
        return self.programdata

    def inlas_kombinationer(self, textfile):
        """"Funktion som läser in de bra knapptryckskombinationerna och lägger till dessa i en lista som returneras"""
        with open(textfile, 'r', encoding='utf8') as file:
            numbers = file.readlines()
            for line in numbers:
                row = []
                number_list = line.strip()
                for i in number_list:
                    number = int(i)
                    row.append(number)
                self.order.append(row[:])
                row.clear()
        return self.order

    def spara(self, colour, size, order, datum):
        """Funktion som sparar senaste tre knapptryckningarna, datum samt storlek och färg på Tamagotchin"""
        str_int = [str(i) for i in order]
        orderstr = ''.join(str_int)
        with open("egenskaper.txt.", 'w', encoding='utf8') as file:
            file.write(colour + "\n" + str(size) + "\n" + orderstr + "\n" + datum + "\n")


def main():
    """Skapar fönstret för Tamagotchin och anropar klassen för Tamagotchin, samt den som läser in och sparar data"""
    rot = Tk()
    egenskaper = Data().inlas("egenskaper.txt")
    good_outcomes = Data().inlas_kombinationer("goodoutcomes.txt")
    djur = Tamagotchi(rot, egenskaper[0], egenskaper[1], egenskaper[2], egenskaper[3], good_outcomes)
    rot.mainloop()
    Data().spara(djur.colour, djur.size, djur.ordning, str(time.time()))


if __name__ == '__main__':
    main()
