import matplotlib.pyplot as plt
import matplotlib
import os
import tkinter as Tk
import random as rd
import numpy as np
from PIL import Image,ImageTk
matplotlib.use('TkAgg')



def update_result():
    pass


def get_leaderboard():
    pass


def store_result():
    pass


def build_plot(plot_numbers):
    # generate random numbers
    xx = np.array([0, 1])
    yy = np.array([0, 1])
    means = [xx.mean(), yy.mean()]
    stds = [xx.std() / 3, yy.std() / 3]
    corr = rd.random()  # correlation
    covs = [[stds[0] ** 2, stds[0] * stds[1] * corr],
            [stds[0] * stds[1] * corr, stds[1] ** 2]]
    m = np.random.multivariate_normal(means, covs, plot_numbers).T
    list_x = m[0]
    list_y = m[1]
    plt.scatter(list_x, list_y, s=1, c="black", alpha=1)
    plt.axis([0, 1, 0, 1])
    plt.savefig(os.getcwd() + '\plot.png')
    plt.clf()
    return corr

class GuessTheCorrelation:
    def __init__(self, master):
        self.master = master
        master.title("Guess the correlation")
        master.geometry("700x700")
        self.canvas = Tk.Canvas()
        self.canvas.pack(side='top', fill='both', expand='yes')

        self.button = Tk.Button(master=root, text='Quit', command=master.quit)
        self.button.pack(side=Tk.BOTTOM)

        self.label1 = Tk.Label(root, textvariable="Correlation:", height=2)
        self.label1.pack(side=Tk.BOTTOM)

        self.text1 = Tk.Text(root, height=2, width=50)
        self.text1.pack(side=Tk.BOTTOM)

        self.text2 = Tk.Text(root, height=2, width=50)
        self.text2.pack(side=Tk.BOTTOM)

        self.box1 = Tk.Entry(root, bd=4, textvariable=Tk.StringVar())
        self.box1.pack(side=Tk.BOTTOM)

        self.input_button = Tk.Button(root, text="Check", command=self.check_correlation, width=5)
        self.input_button.pack(side=Tk.BOTTOM)

        self.refresh_button = Tk.Button(root, text="Refresh", command=self.refresh, width=5)
        self.refresh_button.pack(side=Tk.BOTTOM)

        self.corr = float(build_plot(100))
        self.photo = ImageTk.PhotoImage(Image.open(os.getcwd() + '\plot.png'))
        self.checked = 0

        self.my_img = self.canvas.create_image(10, 10, image=self.photo, anchor='nw')

    def check_correlation(self):
        self.text1.delete(1.0, Tk.END)
        self.text2.delete(1.0, Tk.END)
        try:
            guess = float(self.box1.get())
            if self.checked == 0:
                self.checked = 1
                self.text1.insert(Tk.END, "True correlation: " + str(self.corr))
                self.text2.insert(Tk.END, "Fault: " + str(self.corr - guess))
            else:
                self.refresh()
        except ValueError:
            pass

    def refresh(self):
        self.box1.delete(0, Tk.END)
        self.text1.delete(1.0, Tk.END)
        self.text2.delete(1.0, Tk.END)
        self.corr = float(build_plot(100))
        self.photo = ImageTk.PhotoImage(Image.open(os.getcwd() + '\plot.png'))
        self.canvas.itemconfigure(self.my_img, image=self.photo)


if __name__ == "__main__":
    root = Tk.Tk()
    GuessTheCorrelation(root)
    root.mainloop()
