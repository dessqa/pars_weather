import requests
import json
import datetime
import time

api_key = "7d2b41f7cad5e4fafd00596481ea396c"
lat = "48.208490"
lon = "16.3720800"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
response = requests.get(url)
data = json.loads(response.text)
# print(data)


current = data["current"]["temp"]
date = data["current"]["dt"]
# print(current)

hourly = data["daily"]

l = []  # для разницы
raznica = []
dat = []  # для дат
tempp = []  # для температуры по ощущениям ночью
fl = []  # для температуры ночью
for entry in hourly:
    timestamp = entry['dt']
    date = datetime.datetime.fromtimestamp(timestamp)
    for j in range(0, 1):
        dat.append(date)
    temp = entry["temp"]["night"]  # температура ночью
    for j in range(0, 1):
        tempp.append(temp)
    feels_like = entry["feels_like"]["night"]  # температура "по ощущениям" ночью
    for j in range(0, 1):
        fl.append(feels_like)
    raznica = feels_like - temp
    # print(raznica)
    print(f"{date:%Y-%m-%d}", temp, feels_like, round(raznica, 2))
    for i in range(0, 1):
        l.append(raznica)  # массив с разницами
        sortirovka = sorted(l)  # сортировка от мин к мах

ind = l.index(sortirovka[7])

print('Минимальная разница между ощущаемой температурой', fl[ind], ' и температурой ночью', tempp[ind], ' в ',
      round(sortirovka[7], 2), 'градуса прогнозируется', f"{dat[ind]:%Y-%m-%d}")

raznicaa = []
datt = []
ss = []
sr = []
rz = []
lll = []
for _entry in hourly:
    timestamp = _entry['dt']
    datee = datetime.datetime.fromtimestamp(timestamp)
    for jj in range(0, 1):
        datt.append(datee)
    sunset = _entry["sunset"]  # восход
    sunset_input = datetime.datetime.fromtimestamp(sunset)  # для вывода
    for jj in range(0, 1):
        ss.append(sunset)
    sunrise = _entry["sunrise"]  # закат
    sunrise_input = datetime.datetime.fromtimestamp(sunrise)  # для вывода
    for jj in range(0, 1):
        sr.append(sunrise)
    rz = sunset - sunrise - 21600
    rz_input = datetime.datetime.fromtimestamp(rz)
    print(f"{datee:%Y-%m-%d}", f"{sunrise_input:%H:%M:%S}", f"{sunset_input:%H:%M:%S}", f"{rz_input:%H:%M:%S}")
    for ii in range(0, 1):
        lll.append(rz)  # массив с разницами
        sortirovka_lll = sorted(lll)  # сортировка от мин к мах

ind_2 = lll.index(sortirovka_lll[7])

print('Максимальная продолжительность светового дня ожидается ', f"{datt[ind_2]:%Y-%m-%d}")
