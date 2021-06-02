import tkinter as tk
from tkinter import ttk
import numpy as np 
import pickle
class CarPrediction(tk.Tk):
    def __init__(self):
        super().__init__()
        width = 410
        height = 400
        self.geometry(f"{width}x{height}")
        self.minsize(width,height)
        self.maxsize(width,height)
        self.title('Car Prediction Model')
    def Header(self):
        Heading = tk.Label(text='Car Prediction Model',font='arial 18 bold')
        Heading.place(x=85,y=10)
        # Importing Model ---------------
        with open('CarPredictionModel','rb') as P_Model:
            self.Model = pickle.load(P_Model)
        with open('VariableInfo', 'rb') as varinfo:
            self.varinfo = pickle.load(varinfo)
        with open('VariableDict', 'rb') as vardict:
            self.varlen = pickle.load(vardict)
        # ----------------------------
    def command_button(self):
        pass
    def body(self):
        self.F1 = tk.Frame(self)
        self.F1.place(x=90,y=60)
        self.F2 = tk.Frame(self)
        self.F2.place(x=90,y=90)
        self.F3 = tk.Frame(self)
        self.F3.place(x=90,y=120)
        self.F4 = tk.Frame(self)
        self.F4.place(x=90,y=150)
        self.F5 = tk.Frame(self)
        self.F5.place(x=90,y=180)
        self.F6 = tk.Frame(self)
        self.F6.place(x=90, y=210)
        self.F7 = tk.Frame(self)
        self.F7.place(x=90, y=240)
        self.F8 = tk.Frame(self)
        self.F8.place(x=90, y=270)
        self.F9 = tk.Frame(self)
        self.F9.place(x=175, y=305)
        self.F10 = tk.Frame(self,bg='gray')
        self.F10.place(x=120, y=340)
        # ---------------------- Manufacture Ins
        self.Manu_var = tk.StringVar()
        self.Manu_var.set('Audi')
        self.Manu_choices = list(self.varlen.keys())
        self.Manu_Label = tk.Label(self.F1,text='Manufacture:-',font='arial 12')
        self.Manu_Label.pack(side=tk.LEFT, padx=(0,20))
        self.Manudown = ttk.Combobox(self.F1,value=self.Manu_choices)
        self.Manudown.current(0)
        self.Manudown.bind("<<ComboboxSelected>>", self.Menuchange)
        self.Manudown.pack(side=tk.LEFT)
        #------------------------- Model Ins
        self.model_var = tk.StringVar()
        self.model_var.set('Audi')
        self.model_choices = list(self.varlen[self.Manudown.get()])
        self.model_Label = tk.Label(self.F2, text='Model:-', font='arial 12')
        self.model_Label.pack(side=tk.LEFT, padx=(0, 63))
        self.modeldown = ttk.Combobox(self.F2, value=self.model_choices)
        self.modeldown.current(0)
        # self.modeldown.bind("<<ComboboxSelected>>", self.Menuchange)
        self.modeldown.pack(side=tk.LEFT)
        #------------------------- Year Ins
        self.Year_var = tk.IntVar()
        self.Year_var.set(2017)
        self.Year_Label = tk.Label(self.F3, text='Year:-   ', font='arial 12')
        self.Year_Label.pack(side=tk.LEFT, padx=(0, 63))
        self.Year_ent = ttk.Entry(self.F3, textvariable=self.Year_var)
        self.Year_ent.pack()
        #----------------------------- Milage Ins
        self.Milage_var = tk.IntVar()
        self.Milage_var.set(16000)
        self.Milage_Label = tk.Label(self.F4, text='Mileage:-', font='arial 12')
        self.Milage_Label.pack(side=tk.LEFT, padx=(0, 50))
        self.Milage_ent = ttk.Entry(self.F4, textvariable=self.Milage_var)
        self.Milage_ent.pack()
        # --------------------------- tax Ins
        self.tax_var = tk.IntVar()
        self.tax_var.set(150)
        self.tax_Label = tk.Label(self.F5, text='Tax:-     ', font='arial 12')
        self.tax_Label.pack(side=tk.LEFT, padx=(0, 63))
        self.tax_ent = ttk.Entry(self.F5, textvariable=self.tax_var)
        self.tax_ent.pack()
        # ----------------------------- Mpg ins
        self.mpg_var = tk.IntVar()
        self.mpg_var.set(55.4)
        self.mpg_Label = tk.Label(self.F6, text='Mpg:-   ', font='arial 12')
        self.mpg_Label.pack(side=tk.LEFT, padx=(0, 63))
        self.mpg_ent = ttk.Entry(self.F6, textvariable=self.mpg_var)
        self.mpg_ent.pack()
        # ------------------------ Engine Size Ins
        self.engine_var = tk.IntVar()
        self.engine_var.set(1.4)
        self.engine_Label = tk.Label(self.F7, text='Engine Size:-', font='arial 12')
        self.engine_Label.pack(side=tk.LEFT, padx=(0, 25))
        self.engine_ent = ttk.Entry(self.F7, textvariable=self.engine_var)
        self.engine_ent.pack()
        # ------------------------ Transmission Ins
        self.trans_var = tk.StringVar()
        self.trans_var.set('Automatic')
        self.trans_choices = ['Automatic','Manual','Semi-Auto']
        self.trans_Label = tk.Label(self.F8, text='Transmission:-', font='arial 12')
        self.trans_Label.pack(side=tk.LEFT, padx=(0, 15))
        self.transdown = ttk.Combobox(self.F8, value=self.trans_choices)
        self.transdown.current(0)
        # self.transdown.bind("<<ComboboxSelected>>", self.Menuchange)
        self.transdown.pack(side=tk.LEFT)
        # ------------------------------------------------- # --------- Button
        self.Predict_prices = ttk.Button(self.F9, text='Predict Prices', command=self.Button)
        self.Predict_prices.pack()
        # ----------------------------------------------- Predicted Label
        self.PredictLabel = ttk.Label(self.F10, text='')
        self.PredictLabel.pack()
    def Menuchange(self,event):
        self.model_choices = list(self.varlen[self.Manudown.get()])
        self.modeldown.config(value=self.model_choices)
        self.modeldown.current(0)
    def Button(self):
        Manufacture = self.Manudown.get()
        Model = self.modeldown.get()
        Year = self.Year_var.get()
        Mileage= self.Milage_var.get()
        Tax = self.tax_var.get()
        Mpg  = self.mpg_var.get()
        Engine = self.engine_var.get()
        Transmission = self.transdown.get()
        Ideal = self.varinfo
        def PredictCarPrice(manu, model, year, trans, milag, tax, mpg, Engsize):
            st = np.zeros(170)
            ide = Ideal
            for i in range(6):  # for Company
                if manu == ide[i]:
                    st[i] = 1
            for i in range(6, 164):
                if model == ide[i]:
                    st[i] = 1
            st[163] = year
            st[164] = milag
            st[165] = tax
            st[166] = mpg
            st[167] = Engsize
            for i in range(168, 170):
                if trans == ide[i]:
                    st[i] = 1
            return [st]
        arrayfinal = PredictCarPrice(Manufacture, Model, Year, Transmission, Mileage, Tax, Mpg, Engine)
        Predicted_Value = self.Model.predict(arrayfinal)
        self.PredictLabel.config(text=f"Predicted Price : {round(Predicted_Value[0],3)}",font='arial 11 bold')
    def footer(self, YesP,NoP):
        pass
if __name__ == '__main__':
    Model = CarPrediction()
    Model.Header()
    Model.body()
    Model.Button()

    Model.mainloop()

