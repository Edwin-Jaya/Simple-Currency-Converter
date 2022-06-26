from tkinter import *

# Code to make a window
root = Tk()
# Code to set the size of the window
root.geometry("300x300")
# Code to print the title of your window
root.title("Simple Currency Converter")
# Code to print/set a label
desc=Label(root,text="Welcome to the simple currency converter!\n Made by Edwin Jaya")
# Code to set the position of an object auto
desc.pack(pady=9)
# Code to store the radiobutton varible
v=StringVar(root,"0")
# Radiobutton key and values
choices_values={"Idr To Eng":"1",
                "Eng To Idr":"2"}
# Code to iterate the key and values in dict
for(text,value) in choices_values.items():
    Radiobutton(root,text=text,variable=v,value=value).pack(side=TOP, ipady=5)
# Function that'd run when we click the process button
def convertValue():
    if(v.get()=="1"):
        try:
            convertedToIntValue = int(value_entry.get())
            finalConvertedValue = convertedToIntValue*0.000067
            stringValue=str(finalConvertedValue)
            displayValue=0
            if(len(stringValue)>=7):
                displayValue='{0:.6f}'.format(finalConvertedValue)
            else:
                displayValue=stringValue
            result_label.config(text=displayValue+" USD")
        except:
            result_label.config(text="Please input a number")
    elif(v.get()=="2"):
        try:
            convertedToIntValue = int(value_entry.get())
            finalConvertedValue = convertedToIntValue*14829.50
            stringValue=str(finalConvertedValue)
            displayValue=0
            if(len(stringValue)>=7):
                displayValue='{0:.2f}'.format(finalConvertedValue)
            else:
                displayValue=stringValue
            result_label.config(text=displayValue+" IDR")
        except:
            result_label.config(text="Please input a number")

# Code to make label and entry
value_label=Label(root,text="Insert the amount of value")
value_entry=Entry(root, width=25)
desc_label=Label(root,text="Result")
result_label=Label(root,text=" ")
btn=Button(root, text="Process", command=convertValue)

# Code to set the position of an obj auto
value_label.pack(pady=10)
value_entry.pack(pady=5)
desc_label.pack(pady=5)
result_label.pack()
btn.pack(pady=10)


# Code to loop the main program
root.mainloop()