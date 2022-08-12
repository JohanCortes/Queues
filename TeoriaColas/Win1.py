import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import BOLD
import asyncio
from Colas import Cola
from Poblacion import Poblacion
from Win2 import Ventana2


class Ventana(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.bcolor = "#bfcfef"
        self.config(width=1000, height=650, bg=self.bcolor)
        self.colas = []
        self.poblacion = None
        self.create_widgets()

    def create_widgets(self):
        self.label1 = tk.Label(self, text="λ = ", font=(
            "Calibri", 13, BOLD), bg=self.bcolor)
        self.label1.place(relx=0.02, rely=0.05)
        self.spinbox1 = tk.Spinbox(
            self, from_=0, to=10000, font=("Calibri", 13), bg="white")
        self.spinbox1.place(relx=0.05, rely=0.05, relwidth=0.07)
        self.l1 = tk.Label(self, text="Clien/h",
                           font=("Calibri", 12), bg=self.bcolor)
        self.l1.place(relx=0.12, rely=0.05)
        self.label2 = tk.Label(self, text="μ = ", font=(
            "Calibri", 13, BOLD), bg=self.bcolor)
        self.label2.place(relx=0.21, rely=0.05)
        self.spinbox2 = tk.Spinbox(
            self, from_=0, to=10000, font=("Calibri", 13), bg="white")
        self.spinbox2.place(relx=0.24, rely=0.05, relwidth=0.07)
        self.l2 = tk.Label(self, text="Clien/h",
                           font=("Calibri", 12), bg=self.bcolor)
        self.l2.place(relx=0.31, rely=0.05)
        self.label3 = tk.Label(self, text="σ = ", font=(
            "Calibri", 13, BOLD), bg=self.bcolor)
        self.label3.place(relx=0.4, rely=0.05)
        self.spinbox3 = tk.Spinbox(
            self, from_=0, to=10000, font=("Calibri", 13), bg="white")
        self.spinbox3.place(relx=0.43, rely=0.05, relwidth=0.07)
        self.l3 = tk.Label(self, text="horas", font=(
            "Calibri", 12), bg=self.bcolor)
        self.l3.place(relx=0.5, rely=0.05)
        self.label4 = tk.Label(self, text="N = ", font=(
            "Calibri", 13, BOLD), bg=self.bcolor)
        self.label4.place(relx=0.57, rely=0.05)
        self.spinbox4 = tk.Spinbox(
            self, from_=1, to=1000, font=("Calibri", 13), bg="white")
        self.spinbox4.place(relx=0.60, rely=0.05, relwidth=0.06)
        self.l4 = tk.Label(self, text="Clientes",
                           font=("Calibri", 12), bg=self.bcolor)
        self.l4.place(relx=0.66, rely=0.05)
        self.label5 = tk.Label(self, text="I = ", font=(
            "Calibri", 13, BOLD), bg=self.bcolor)
        self.label5.place(relx=0.75, rely=0.05)
        self.spinbox5 = tk.Spinbox(
            self, from_=1, to=100, font=("Calibri", 13), bg="white")
        self.spinbox5.place(relx=0.775, rely=0.05, relwidth=0.05)
        self.l5 = tk.Label(self, text="Iterac.",
                           font=("Calibri", 12), bg=self.bcolor)
        self.l5.place(relx=0.825, rely=0.05)

        self.button1 = tk.Button(self, text="Generar", font=(
            "Calibri", 13, BOLD), bg="#55F", fg="#DDD", border=2, command=self.click1)
        self.button1.place(relx=0.9, rely=0.04, relwidth=0.08)

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.lista = tk.Listbox(self, font=(
            "Calibri", 13), bg="white", border=2, yscrollcommand=scrollbar.set)
        self.lista.place(relx=0.07, rely=0.15, relwidth=0.185, relheight=0.7)
        scrollbar.config(command=self.lista.yview)
        scrollbar.place(relx=0.255, rely=0.15, relheight=0.7)

        self.button2 = tk.Button(self, text="Detalles", font=(
            "Calibri", 13, BOLD), bg="#55F", fg="#DDD", border=2, command=self.click2)
        self.button2.place(relx=0.07, rely=0.88, relwidth=0.2)

        self.container = tk.LabelFrame(
            self, font=("Calibri", 13), bg=self.bcolor)
        self.container.place(relx=0.35, rely=0.15,
                             relwidth=0.58, relheight=0.78)

        self.combo = ttk.Combobox(self.container, font=(
            "Calibri", 13), state="readonly")
        self.combo.place(relx=0.15, rely=0.04, relwidth=0.48)
        self.combo['values'] = ("Tiempo entre llegada promedio",
                                "Momento ultima llegada", "Tiempo inicio del ultimo servicio", "Tiempo de servicio promedio", "Tiempo terminacion ultimo servicio", "Tiempo espera promedio", "Tiempo total de espera", "Tiempo en operacion", "Porcentaje de operacion")
        self.button3 = tk.Button(self.container, text="Calcular", font=(
            "Calibri", 13, BOLD), bg="#55F", fg="#DDD", border=2, command=self.click3)
        self.button3.place(relx=0.75, rely=0.03, relwidth=0.15)

        self.min = tk.Label(self.container, text="Minimo = ",
                            font=("Calibri", 14), bg=self.bcolor)
        self.min.place(relx=0.09, rely=0.15)
        self.max = tk.Label(self.container, text="Maximo = ",
                            font=("Calibri", 14), bg=self.bcolor)
        self.max.place(relx=0.09, rely=0.24)
        self.media = tk.Label(self.container, text="Media = ",
                              font=("Calibri", 14), bg=self.bcolor)
        self.media.place(relx=0.09, rely=0.33)
        self.des = tk.Label(self.container, text="Desviación = ",
                            font=("Calibri", 14), bg=self.bcolor)
        self.des.place(relx=0.09, rely=0.42)
        self.var = tk.Label(self.container, text="Varianza = ",
                            font=("Calibri", 14), bg=self.bcolor)
        self.var.place(relx=0.09, rely=0.51)
        self.IC = tk.Label(self.container, text="IC₍₁₎ = ",
                           font=("Calibri", 14), bg=self.bcolor)
        self.IC.place(relx=0.09, rely=0.6)
        self.IIC = tk.Spinbox(self.container, from_=1, to=99, font=(
            "Calibri", 13), bg="white")
        self.IIC.place(relx=0.8, rely=0.60, relwidth=0.09)
        self.tdist = tk.Label(self.container, text="Tipo de distribución: ", font=(
            "Calibri", 14), bg=self.bcolor, fg="blue", cursor="hand2")
        self.tdist.place(relx=0.09, rely=0.69)
        self.tdist.bind("<Button-1>", lambda e: self.clicktdist())
        self.corr = tk.Label(self.container, text="Correlación = ", font=(
            "Calibri", 14), bg=self.bcolor)
        self.corr.place(relx=0.09, rely=0.78)

        self.button4 = tk.Button(self.container, text="Graficar", font=(
            "Calibri", 13, BOLD), bg="#55F", fg="#DDD", border=2, command=self.click4)
        self.button4.place(relx=0.425, rely=0.89, relwidth=0.15)

    async def generar_colas(self, lam, mu, sig, n, i):
        self.colas = []
        self.lista.delete(0, tk.END)
        while self.colas.__len__() < i:
            cola = Cola(lam=lam, mu=mu, sig=sig, n=n)
            await asyncio.sleep(0.01)
            if cola.statistic()['po'][0] != 0:
                self.colas.append(cola)
                self.lista.insert(tk.END, 'Cola '+str(self.colas.__len__()))

    def click1(self):
        lam = float(self.spinbox1.get())
        mu = float(self.spinbox2.get())
        sig = float(self.spinbox3.get())
        n = int(self.spinbox4.get())
        i = int(self.spinbox5.get())
        asyncio.run(self.generar_colas(lam, mu, sig, n, i))

    def click2(self):
        if self.lista.size() > 0:
            win2 = Ventana2(tk.Tk(), self.colas[self.lista.curselection()[0]],
                            self.lista.curselection()[0])
            win2.mainloop()

    def click3(self):
        keys = {'Tiempo entre llegada promedio': 'telp', 'Momento ultima llegada': 'mul',
                'Tiempo inicio del ultimo servicio': 'tius', 'Tiempo de servicio promedio': 'tsp',
                'Tiempo terminacion ultimo servicio': 'ttus', 'Tiempo espera promedio': 'tep',
                'Tiempo total de espera': 'tte', 'Tiempo en operacion': 'teo', 'Porcentaje de operacion': 'po'}
        if self.combo.get() != '':
            ic = ''
            for i in self.IIC.get():
                ic += chr(int(i)+8320)
            self.poblacion = Poblacion(
                list(map(lambda x: x.statistic(), self.colas)), self.colas.__len__())
            statistic = self.poblacion.cal(
                keys[self.combo.get()], float(self.IIC.get())/100)
            units = self.colas[0].statistic()[keys[self.combo.get()]][1]
            self.min.config(text="Minimo = "+str(statistic[0])+" "+units)
            self.max.config(text="Maximo = "+str(statistic[1])+" "+units)
            self.media.config(text="Media = "+str(statistic[2])+" "+units)
            self.des.config(text="Desviación = "+str(statistic[3]))
            self.var.config(text="Varianza = "+str(statistic[4]))
            self.IC.config(text="IC₍"+ic+"₎ = "+str(statistic[5]))
            self.tdist.config(text="Tipo de distribución: "+statistic[6])
            self.corr.config(text="Correlación = "+str(statistic[7]))

    def click4(self):
        if self.poblacion is not None and self.colas.__len__() > 0:
            self.poblacion.graph()

    def clicktdist(self):
        if self.poblacion is not None and self.colas.__len__() > 0:
            self.poblacion.graph_tdist()


root = tk.Tk()
app = Ventana(root)
app.mainloop()
