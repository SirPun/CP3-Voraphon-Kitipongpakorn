from tkinter import*
import math

def leftClick(event):
    bmiResult = (float(textBoxWeight.get())/math.pow(((float(textBoxHeight.get()))/100),2))
    print(bmiResult)
    labelResult.configure(text ="%.3f"%bmiResult)
    if bmiResult <= 18.50:
        TrueResult = "อยู่ในเกณฑ์น้ำหนักน้อย / ผอม"
    elif bmiResult <= 22.90:
        TrueResult = "อยู่ในเกณฑ์ปกติ (สุขภาพดี)"
    elif bmiResult <= 24.90:
        TrueResult = "อยู่ในเกณฑ์ท้วม / โรคอ้วนระดับ 1"
    elif bmiResult <= 29.90:
        TrueResult = "อยู่ในเกณฑ์อ้วน / โรคอ้วนระดับ 2"
    elif bmiResult > 29.90:
        TrueResult = "อยู่ในเกณฑ์อ้วนมาก / โรคอ้วนระดับ 3"
    labelTrueResult.configure(text=TrueResultValue)

MainWindow = Tk()
labelHeight = Label(MainWindow,text = "Height (cm)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text = "Weight (kg)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "Calculate")
calculateButton.grid(row=2)
calculateButton.bind("<Button-1>",leftClick)
labelResult =Label(MainWindow,text = "Result" )
labelResult.grid(row=2,column=1)
labelTrueResult = Label(MainWindow,text = "Your body")
labelTrueResult.grid(row=3,column=1)
MainWindow.mainloop()
