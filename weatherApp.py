import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from tkinter.messagebox import showerror
import datetime


today = datetime.datetime.today()
one_day_later = today + datetime.timedelta(days= 1)
two_day_later = today + datetime.timedelta(days= 2)
three_day_later = today + datetime.timedelta(days= 3)
four_day_later = today + datetime.timedelta(days= 4)


day_name = today.strftime("%A")

def get_weather_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            json_data = response.json()
            change_image(json_data["weather"][0]["main"])
            
            return json_data
        except ValueError:
            print("Error: The response is not in JSON format.")
            return None
    else:
        print(f"Error: Unable to fetch data. HTTP Status code: {response.status_code}")
        return None
    
def get_future_weather_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            json_data = response.json()
            return json_data
        except ValueError:
            print("Error: The response is not in JSON format.")
            return None
    else:
        print(f"Error: Unable to fetch data. HTTP Status code: {response.status_code}")
        return None

main_frame = tk.Tk()
middle_frame = tk.Frame(main_frame, border= 1)
main_frame.geometry("400x600")
main_frame.resizable(False, False)

main_frame.title("Weather")
final_image = ImageTk.PhotoImage(Image.open("summer.png").resize((250,250), Image.LANCZOS))

def change_image(conditions):
    global final_image
    global label2
    condition = conditions.lower()
    if condition == "clear":
        final_image = ImageTk.PhotoImage(Image.open("summer.png").resize((250,250), Image.LANCZOS))
    elif condition == "rain":
        final_image = ImageTk.PhotoImage(Image.open("rain.png").resize((250,250), Image.LANCZOS))
    elif condition == "clouds":
        final_image = ImageTk.PhotoImage(Image.open("cloud.png").resize((250,250), Image.LANCZOS))
    elif condition == "haze":
        final_image = ImageTk.PhotoImage(Image.open("haze.png").resize((250,250), Image.LANCZOS))
    elif condition == "snow":
        final_image = ImageTk.PhotoImage(Image.open("snow.png").resize((250,250), Image.LANCZOS))
    elif condition == "smoke":
        final_image = ImageTk.PhotoImage(Image.open("smoke.png").resize((250,250), Image.LANCZOS))
    elif condition == "mist":
        final_image = ImageTk.PhotoImage(Image.open("haze.png").resize((250,250), Image.LANCZOS))

    label2 = tk.Label(middle_frame, image=final_image, bg= background_color)
    label2.grid(row= 0, column= 0, sticky= "snew")


background_color = "lightblue"

city_name = "Los Angeles"
unit = "imperial"
api_key = ""
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={unit}'
forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units={unit}"

weather_data = get_weather_data(url)["main"]
future_weather_data = get_future_weather_data(forecast_url)["list"]

weather_f = int(weather_data["temp"])
high_f = int(weather_data["temp_max"])
low_f = int(weather_data["temp_min"])

weather_f_1 = int(future_weather_data[1]["main"]["temp"])
high_f_1 = int(future_weather_data[1]["main"]["temp_max"])
low_f_1 = int(future_weather_data[1]["main"]["temp_min"])

weather_f_2 = int(future_weather_data[2]["main"]["temp"])
high_f_2 = int(future_weather_data[2]["main"]["temp_max"])
low_f_2 = int(future_weather_data[2]["main"]["temp_min"])

weather_f_3 = int(future_weather_data[3]["main"]["temp"])
high_f_3 = int(future_weather_data[3]["main"]["temp_max"])
low_f_3 = int(future_weather_data[3]["main"]["temp_min"])

weather_f_4 = int(future_weather_data[4]["main"]["temp"])
high_f_4 = int(future_weather_data[4]["main"]["temp_max"])
low_f_4 = int(future_weather_data[4]["main"]["temp_min"])

weather_f_1_final = f"{one_day_later.strftime("%A")}: {weather_f_1}° F (H: {high_f_1}° F, L: {low_f_1}° F)"
weather_f_2_final = f"{two_day_later.strftime("%A")}: {weather_f_2}° F (H: {high_f_2}° F, L: {low_f_2}° F)"
weather_f_3_final = f"{three_day_later.strftime("%A")}: {weather_f_3}° F (H: {high_f_3}° F, L: {low_f_3}° F)"
weather_f_4_final = f"{four_day_later.strftime("%A")}: {weather_f_4}° F (H: {high_f_4}° F, L: {low_f_4}° F)"

weather = f"{weather_f}° F (H: {high_f}° F, L: {low_f}° F)"

def weather_changer(city_name_in_func):
    global weather_f
    global high_f
    global low_f
    global weather
    global weather_f_1_final
    global weather_f_2_final
    global weather_f_3_final
    global weather_f_4_final

    unit = "imperial"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name_in_func}&appid=bbc971b945144354a2a230eceaac35a9&units={unit}'
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name_in_func}&appid=bbc971b945144354a2a230eceaac35a9&units={unit}"

    data_today = get_weather_data(url)["main"]
    data_future = get_future_weather_data(forecast_url)["list"]

    weather_f = int(data_today["temp"])
    high_f = int(data_today["temp_max"])
    low_f = int(data_today["temp_min"])

    weather_f_1 = int(data_future[1]["main"]["temp"])
    high_f_1 = int(data_future[1]["main"]["temp_max"])
    low_f_1 = int(data_future[1]["main"]["temp_min"])

    weather_f_2 = int(data_future[2]["main"]["temp"])
    high_f_2 = int(data_future[2]["main"]["temp_max"])
    low_f_2 = int(data_future[2]["main"]["temp_min"])

    weather_f_3 = int(data_future[3]["main"]["temp"])
    high_f_3 = int(data_future[3]["main"]["temp_max"])
    low_f_3 = int(data_future[3]["main"]["temp_min"])

    weather_f_4 = int(data_future[4]["main"]["temp"])
    high_f_4 = int(data_future[4]["main"]["temp_max"])
    low_f_4 = int(data_future[4]["main"]["temp_min"])

    day1str.set(f"{one_day_later.strftime("%A")}: {weather_f_1}° F (H: {high_f_1}° F, L: {low_f_1}° F)")
    day2str.set(f"{two_day_later.strftime("%A")}: {weather_f_2}° F (H: {high_f_2}° F, L: {low_f_2}° F)")
    day3str.set(f"{three_day_later.strftime("%A")}: {weather_f_3}° F (H: {high_f_3}° F, L: {low_f_3}° F)")
    day4str.set(f"{four_day_later.strftime("%A")}: {weather_f_4}° F (H: {high_f_4}° F, L: {low_f_4}° F)")

    weather_label_str.set(f"{weather_f}° F (H: {high_f}° F, L: {low_f}° F)") 


def change_city_func():
    def close_and_update():
        city_name_str.set(entry_str.get())
        weather_changer(entry_str.get())
        second_window.destroy()

    second_window = tk.Toplevel(main_frame)
    second_window.geometry("300x100+100+100")
    second_window.title("Change City")
    second_window.resizable(False, False)
    second_window.rowconfigure((0,1), weight= 1)
    second_window.columnconfigure(0, weight= 1)


    entry_str = tk.StringVar()
    entry = tk.Entry(second_window, textvariable= entry_str)
    entry.grid(row= 0, column= 0, pady=10, sticky= "snew")

    button = tk.Button(second_window, text="Submit", command=close_and_update)
    button.grid(row = 1, column= 0, sticky= "snew")

def f_or_c():
    global weather
    if check_var.get() == "c":
        weather_c = int((weather_f - 32) * 5/9)
        high_c = int((high_f - 32) * 5/9)
        low_c = int((low_f - 32) * 5/9)

        weather_c_1 = int((weather_f_1 - 32) * 5/9)
        high_c_1 = int((high_f_1 - 32) * 5/9)
        low_c_1 = int((low_f_1 - 32) * 5/9)

        weather_c_2 = int((weather_f_2 - 32) * 5/9)
        high_c_2 = int((high_f_2 - 32) * 5/9)
        low_c_2 = int((low_f_2 - 32) * 5/9)

        weather_c_3 = int((weather_f_3 - 32) * 5/9)
        high_c_3 = int((high_f_3 - 32) * 5/9)
        low_c_3 = int((low_f_3 - 32) * 5/9)

        weather_c_4 = int((weather_f_4 - 32) * 5/9)
        high_c_4 = int((high_f_4 - 32) * 5/9)
        low_c_4 = int((low_f_4 - 32) * 5/9)

        weather_label_str.set(f"{weather_c}° C (H: {high_c}° C, L: {low_c}° C)")
        day1str.set(f"{one_day_later.strftime("%A")}: {weather_c_1}° C (H: {high_c_1}° C, L: {low_c_1}° C)")
        day2str.set(f"{two_day_later.strftime("%A")}: {weather_c_2}° C (H: {high_c_2}° C, L: {low_c_2}° C)")
        day3str.set(f"{three_day_later.strftime("%A")}: {weather_c_3}° C (H: {high_c_3}° C, L: {low_c_3}° C)")
        day4str.set(f"{four_day_later.strftime("%A")}: {weather_c_4}° C (H: {high_c_4}° C, L: {low_c_4}° C)")

    else:
        weather_label_str.set(f"{weather_f}° F (H: {high_f}° F, L: {low_f}° F)") 
        day1str.set(value= weather_f_1_final)
        day2str.set(value= weather_f_2_final)
        day3str.set(value= weather_f_3_final)
        day4str.set(value= weather_f_4_final)


main_frame.grid_propagate(False)
main_frame.rowconfigure(0, weight= 1)
main_frame.rowconfigure(1, weight= 6)
main_frame.rowconfigure(2, weight= 4)
main_frame.columnconfigure(0, weight= 1)

top_frame = tk.Frame(main_frame, border= 1, borderwidth=1)
bottom_frame = tk.Frame(main_frame, border= 1)

middle_frame.rowconfigure(0, weight= 6)
middle_frame.rowconfigure(1, weight= 1)
middle_frame.columnconfigure(0, weight= 1)
bottom_frame.rowconfigure((0,1,2,3), weight= 1)
bottom_frame.columnconfigure(0, weight= 1)

menu_bar = tk.Menu()
settings_menu = tk.Menu(menu_bar, tearoff= False)
check_var = tk.StringVar(value= "f")
settings_menu.add_radiobutton(label= "°C", value= "c", variable= check_var, command= f_or_c)
settings_menu.add_separator()
settings_menu.add_radiobutton(label= "°F", value= "f", variable= check_var, command= f_or_c)
change_city = tk.Menu(menu_bar, tearoff= False, postcommand= change_city_func)
menu_bar.add_cascade(label= "Settings", menu= settings_menu)
menu_bar.add_cascade(label= "Change City", menu= change_city)
main_frame.configure(menu=menu_bar)

city_name_str = tk.StringVar()
city_name_str.set(city_name)
label1 = tk.Label(top_frame, bg= background_color, fg= "black", font= "Calibri 25", textvariable= city_name_str)
label2 = tk.Label(middle_frame, image=final_image, bg= background_color)

weather_label_str = tk.StringVar(value= weather)
weather_label = tk.Label(middle_frame, bg = background_color, fg= "black", font= "Calibri 20", textvariable= weather_label_str, border= 1)


day1str = tk.StringVar(value= weather_f_1_final)
day2str = tk.StringVar(value= weather_f_2_final)
day3str = tk.StringVar(value= weather_f_3_final)
day4str = tk.StringVar(value= weather_f_4_final)

label3 = tk.Label(bottom_frame, background= background_color, fg = "black", anchor= "w", padx= 10, border= 1, textvariable= day1str)
label4 = tk.Label(bottom_frame, background= background_color, fg = "black", anchor= "w", padx= 10, border= 1, textvariable= day2str)
label5 = tk.Label(bottom_frame, background= background_color, fg = "black", anchor= "w", padx= 10, border= 1, textvariable= day3str)
label6 = tk.Label(bottom_frame, background= background_color, fg = "black", anchor= "w", padx= 10, border= 1, textvariable= day4str)

label1.pack(expand= True, fill= "both")
label2.grid(row= 0, column= 0, sticky= "snew")
weather_label.grid(row= 1, column= 0, sticky= "snew")


label3.grid(row= 0, column=0, sticky= "nsew")
label4.grid(row= 1, column=0, sticky= "nsew")
label5.grid(row= 2, column=0, sticky= "nsew")
label6.grid(row= 3, column=0, sticky= "nsew")


top_frame.grid(row= 0, column= 0, sticky= "nsew")
middle_frame.grid(row= 1, column= 0, sticky= "nsew")
bottom_frame.grid(row= 2, column= 0, sticky= "nsew")


main_frame.mainloop()