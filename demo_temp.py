from tkinter import*
from tkinter import ttk
import requests

def data_get(): 
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d32af1cb7331679c2dd4c09c959f48fc").json()
    w_label1.config(text=data ["weather"][0] ["main"])

    wb_label1.config(text=data["weather"][0]["description"])
    temp_label.config(text=str(data["main"]["temp"]-273.15))
    per_label1.config(text=data["main"]["pressure"])
     

win = Tk()
win.title("Own Group")
win.config(bg = "Red")
win.geometry('500x540') 


name_label =Label(win,text="Weather App", font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com= ttk.Combobox(win,text="Weather App", values = list_name, font=("Time New Roman",20,"bold"))
com.place(x=25,y=120,height=50,width=450)
city_name = StringVar()



w_label = Label(win,text="Weather Climate", font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="", font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win,text="Weather descrption", font=("Time New Roman",17))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1 = Label(win,text="", font=("Time New Roman",17))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win,text="Tempature", font=("Time New Roman",17))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="", font=("Time New Roman",17))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label = Label(win,text="Pressure", font=("Time New Roman",17))
per_label.place(x=25,y=470,height=50,width=210)

per_label1 = Label(win,text="", font=("Time New Roman",17))
per_label1.place(x=250,y=470,height=50,width=210)

summit_button= Button(win,text="summit", font=("Time New Roman",17,"bold"),command=data_get)
summit_button.place(y=190,height=50,width=100,x=200)




win.mainloop()