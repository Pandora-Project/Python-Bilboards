# This module imports data given by user
import requests


class Bilboard:
    def __init__(self) -> None:
        self.art_Url = 'https://billboard-api2.p.rapidapi.com/artist-100'
        self.bil_Url = 'https://billboard-api2.p.rapidapi.com/hot-100'
        self.request_Key = 'f62882719fmshfe91aa6d30922a8p1093d2jsn8617803222a0'

    def get100art(self):
        """request This function requests top100 artists data"""

        # format of a request
        querystring = {"range": "1-10", "date": "2019-05-11"}

        headers = {
            'x-rapidapi-host': "billboard-api2.p.rapidapi.com",
            'x-rapidapi-key': self.request_Key
        }

        response = requests.request("GET",
                                    self.art_Url,
                                    headers=headers,
                                    params=querystring)

        print(response.text)

        return None

    def get100bil(self):
        """request This function requests top100 bilboard data"""

        # format of a request
        querystring = {"range": "1-10", "date": "2019-05-11"}

        headers = {
            'x-rapidapi-host': "billboard-api2.p.rapidapi.com",
            'x-rapidapi-key': self.request_Key
        }

        response = requests.request(
            "GET", self.bil_Url, headers=headers, params=querystring)

        print(response.text)

        return None
