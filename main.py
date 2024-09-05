import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

#Create a class that inherit QWidget to display them
class WeatherApplication (QWidget):

# created constructor to declare all widgets
    def __init__(self):
        super().__init__()
        self.city_name = QLabel("Enter the name is city: ", self)
        self.type_city = QLineEdit(self)
        self.get_currentweather_button = QPushButton("Display Weather", self)
        self.get_personal_button = QPushButton("PM Accelerator", self)
        self.get_PM_button = QPushButton("Developer Information", self)
        self.temperature = QLabel(self)
        self.emoji = QLabel(self)
        self.weather_desc = QLabel( self)
        self.pm_info_label = QLabel(self)
        self.dev_info_label = QLabel(self)
        self.WeatherUI()


#defining method for UI layout
    def WeatherUI(self):
        self.setWindowTitle("Weather Application")
        # creating widgets
        layout = QVBoxLayout()

        layout.addWidget(self.city_name)
        layout.addWidget(self.type_city)
        layout.addWidget(self.get_currentweather_button)
        layout.addWidget(self.temperature)
        layout.addWidget(self.emoji)
        layout.addWidget(self.weather_desc)
        layout.addWidget(self.get_personal_button)
        layout.addWidget(self.get_PM_button)
        layout.addWidget(self.pm_info_label)
        layout.addWidget(self.dev_info_label)

        #alligning all materials to center

        self.setLayout(layout)

        self.city_name.setAlignment(Qt.AlignCenter)
        self.type_city.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.weather_desc.setAlignment(Qt.AlignCenter)

        #applying Style

        self.city_name.setObjectName("city_name")
        self.type_city.setObjectName("type_city")
        self.get_currentweather_button.setObjectName("get_currentweather_button")
        self.get_personal_button.setObjectName("get_personal_button")
        self.get_PM_button.setObjectName("get_PM_button")
        self.temperature.setObjectName("temperature")
        self.emoji.setObjectName("emoji")
        self.weather_desc.setObjectName("weather")

        self.setStyleSheet(
            """
            QLabel, QPushButton{
                font-family: calibri;
            }
            
            QLabel#city_name{
                font-size: 40px;
                font-family: Segoe UI emoji;
            }
             QLineEdit#type_city{
                font-size: 40px;
                font-family: Segoe UI emoji;
            }

             QPushButton#get_currentweather_button{
                font-size: 25px;
                font-family: Segoe UI emoji;
            }
            }
             QLabel#temperature{
                font-size: 60px;
                font-family: Segoe UI emoji;
            }
            
            QLabel#emoji{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            
            QLabel#weather{
                font-size: 50px;
                font-family: Segoe UI emoji;
            }
            }

             QPushButton#get_personal_button{
                font-family: Segoe UI emoji;
            }
            }

             QPushButton#get_PM_button{
                font-family: Segoe UI emoji;
            }
        

            """
        )
        self.get_currentweather_button.clicked.connect(self.get_weather)
        self.get_personal_button.clicked.connect(self.show_pm_accelerator_info)
        self.get_PM_button.clicked.connect(self.show_dev_info)




#Functionalities

    def get_weather(self):

       api_key = "7860479b2186cc2a6ce6cd4de7674399"
       location = self.type_city.text()
       url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

       try:
           response = requests.get(url)
           response.raise_for_status()
           data = response.json()

           if data["cod"] == 200:
               self.display_weather(data)

       except requests.exceptions.HTTPError:
          self.display_errors("City not Found or Connection Error: \nPlease try again")

    def display_errors(self,message):
        self.temperature.setStyleSheet("font-size: 20px")
        self.temperature.setText(message)
        self.emoji.clear()
        self.weather_desc.clear()

    def display_weather(self, data):

        # To Display Temperature
        self.temperature.setStyleSheet("font-size: 60px")
        temp_k = data["main"]["temp"]

        #Convert Kelvin to Farenheit
        temp_F= (temp_k * 9/5)-459.67

        self.temperature.setText(f"{temp_F: .0f} °F")

        #To display Weather
        weather = data["weather"][0]["description"]
        self.weather_desc.setText(weather)

        # To display Emoji
        display_emoji = data["weather"][0]["id"]
        self.emoji.setText(self.display_emoji(display_emoji))

    #method to display emoji in the UI
    @staticmethod
    def display_emoji(display_emoji):

        if 200 <= display_emoji <= 232:
            return "⛈"
        elif 300 <= display_emoji <= 321:
            return "🌦"
        elif 500 <= display_emoji <= 531:
            return "🌧"
        elif 600 <= display_emoji <= 622:
            return "❄"
        elif 701 <= display_emoji <= 741:
            return "🌫"
        elif display_emoji == 762:
            return "🌋"
        elif display_emoji == 771:
            return "💨"
        elif display_emoji == 781:
            return "🌪"
        elif display_emoji == 800:
            return "☀"
        elif 801 <= display_emoji <= 804:
            return "☁"
        else:
            return ""

    # Display Information About Developer and PM Accelerator

    def show_pm_accelerator_info(self):
        if self.pm_info_label.text():  # If the label already has text, clear it
            self.pm_info_label.clear()
        else:
            program_description = """
            The Product Manager Accelerator Program is designed to support PM professionals through every stage of their career. 
            From students looking for entry-level jobs to Directors looking to take on a leadership role, our program has helped over hundreds of students fulfill their career aspirations.

            Our Product Manager Accelerator community are ambitious and committed. Through our program they have learnt, honed and developed new PM and leadership skills, giving them a strong foundation for their future endeavours.
            """
            self.pm_info_label.setText(program_description)


    def show_dev_info(self):
        if self.dev_info_label.text():  # If the label already has text, clear it
            self.dev_info_label.clear()
        else:
            dev_info = "Name: Ian Gabriel Mondares \nSchool: Bowie State University"
            self.dev_info_label.setText(dev_info)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    WeatherApp = WeatherApplication()
    WeatherApp.show()
    sys.exit(app.exec_())
