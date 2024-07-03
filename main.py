import requests
import json
import win32com.client as wincom

city=input("city name:\n")
url=f"https://api.weatherapi.com/v1/current.json?key=5a1d2f9c063c4194acf150244240207&q={city}"
r=requests.get(url)
print(r.text)
wdic = json.loads(r.text)
w=wdic["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.SpVoice")
text = f" current weather in {city} is {w} degrees"
print(" ",text)
speak.Speak(text)
