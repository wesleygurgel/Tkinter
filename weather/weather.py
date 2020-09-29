from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Weather")
root.geometry("400x400")

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F77CB7A9-5D3C-456B-8F66-10A89899408D

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F77CB7A9-5D3C-456B-8F66-10A89899408D")
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error..."

myLabel = Label(root, text=api[0]['ReportingArea']).pack()

root.mainloop()