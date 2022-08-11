import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
from tkinter.filedialog import asksaveasfile

class Ventana2(tk.Frame):
    def __init__(self, master=None, cola=None, index=0):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.bcolor = "#bfcfef"
        self.config(width=900, height=600, bg=self.bcolor)
        self.index = index
        self.cola = cola
        self.rend = cola.calcular_f()
        self.data = cola.statistic()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, text="Cola "+str(self.index+1),
                              font=("Calibri", 18, BOLD), bg=self.bcolor)
        self.title.place(relx=0.47, rely=0.05)

        self.telp = tk.Label(self, text="Tiempo entre llegada promedio = " + str(self.data['telp'][0])[0:8] + ' ' + self.data['telp'][1],
                             font=("Calibri", 14), bg=self.bcolor)
        self.telp.place(relx=0.05, rely=0.15)

        self.mul = tk.Label(self, text="Momento ultima llegada = " + str(self.data['mul'][0])[0:8] + ' ' + self.data['mul'][1],
                            font=("Calibri", 14), bg=self.bcolor)
        self.mul.place(relx=0.05, rely=0.23)

        self.tius = tk.Label(self, text="Tiempo inicio del ultimo servicio = " + str(self.data['tius'][0])[0:8] + ' ' + self.data['tius'][1],
                             font=("Calibri", 14), bg=self.bcolor)
        self.tius.place(relx=0.05, rely=0.31)

        self.tsp = tk.Label(self, text="Tiempo de servicio promedio = " + str(self.data['tsp'][0])[0:8] + ' ' + self.data['tsp'][1],
                            font=("Calibri", 14), bg=self.bcolor)
        self.tsp.place(relx=0.05, rely=0.39)

        self.ttus = tk.Label(self, text="Tiempo terminacion ultimo servicio = " + str(self.data['ttus'][0])[0:8] + ' ' + self.data['ttus'][1],
                             font=("Calibri", 14), bg=self.bcolor)
        self.ttus.place(relx=0.05, rely=0.47)

        self.tep = tk.Label(self, text="Tiempo de espera promedio = " + str(self.data['tep'][0])[0:8] + ' ' + self.data['tep'][1],
                            font=("Calibri", 14), bg=self.bcolor)
        self.tep.place(relx=0.05, rely=0.55)

        self.tte = tk.Label(self, text="Tiempo total de espera = " + str(self.data['tte'][0])[0:8] + ' ' + self.data['tte'][1],
                            font=("Calibri", 14), bg=self.bcolor)
        self.tte.place(relx=0.05, rely=0.63)

        self.teo = tk.Label(self, text="Tiempo en operacion = " + str(self.data['teo'][0])[0:8] + ' ' + self.data['teo'][1],
                            font=("Calibri", 14), bg=self.bcolor)
        self.teo.place(relx=0.05, rely=0.71)

        self.po = tk.Label(self, text="Porcentaje de operacion = " + str(self.data['po'][0]*100)[0:8] + ' ' + self.data['po'][1],
                           font=("Calibri", 14), bg=self.bcolor)
        self.po.place(relx=0.05, rely=0.79)

        self.rho = tk.Label(self, text="ρ = " + str(self.rend['p']), font=(
            "Calibri", 14), bg=self.bcolor)
        self.rho.place(relx=0.6, rely=0.15)

        self.rho0 = tk.Label(self, text="ρ₀ = " + str(self.rend['p0']), font=(
            "Calibri", 14), bg=self.bcolor)
        self.rho0.place(relx=0.6, rely=0.23)

        self.ls = tk.Label(self, text="Lₛ = " + str(self.rend['ls']) + " clientes", font=(
            "Calibri", 14), bg=self.bcolor)
        self.ls.place(relx=0.6, rely=0.31)

        self.lq = tk.Label(self, text="Lq = " + str(self.rend['lq']) + " clientes", font=(
            "Calibri", 14), bg=self.bcolor)
        self.lq.place(relx=0.6, rely=0.39)

        self.ws = tk.Label(self, text="Wₛ = " + str(self.rend['ws']) + " horas", font=(
            "Calibri", 14), bg=self.bcolor)
        self.ws.place(relx=0.6, rely=0.47)

        self.wq = tk.Label(self, text="Wq = " + str(self.rend['wq']) + " horas", font=(
            "Calibri", 14), bg=self.bcolor)
        self.wq.place(relx=0.6, rely=0.55)

        self.button4 = tk.Button(self, text="Graficar", font=(
            "Calibri", 14, BOLD), bg="#55F", fg="#DDD", border=2, command=self.cola.graph)
        self.button4.place(relx=0.255, rely=0.88, relwidth=0.15)

        self.button5 = tk.Button(self, text="Exportar", font=(
            "Calibri", 14, BOLD), bg="#55F", fg="#DDD", border=2, command=self.click5)
        self.button5.place(relx=0.595, rely=0.88, relwidth=0.15)

    def click5(self):
        s = 'Iteracion,Tasa llegada,Tasa servicio\n'
        for i in range(len(self.cola.poisson)):
            s += str(i+1) + ',' + str(self.cola.poisson[i]) + ',' + str(self.cola.normal[i]) + '\n'
        f = asksaveasfile(initialfile = 'Cola'+str(self.index+1)+'.csv', defaultextension=".csv",filetypes=[("All Files","*.*")])
        if f is None:
            return
        f.write(s)
        f.close()


""" root = tk.Tk()
app = Ventana(root, 1)
app.mainloop() """
