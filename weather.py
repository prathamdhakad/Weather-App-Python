from tkinter import*
from tkinter import ttk

import requests
city_name="Jaipur"
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=d32af1cb7331679c2dd4c09c959f48fc").json()
print(data)