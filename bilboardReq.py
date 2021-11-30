# This module imports data given by user
import requests

# Opening local file containing a auth key so i dont have to type it each time
with open('requestKey.txt') as f:
    local_Req_Key = f.readline()

class Bilboard:
    def __init__(self, request_Key=local_Req_Key):
        self.art_Url = 'https://billboard-api2.p.rapidapi.com/artist-100'
        self.bil_Url = 'https://billboard-api2.p.rapidapi.com/hot-100'
        self.request_Key = request_Key

    def set_request_Key(self, new_request_Key):
        """Setter for request_Key attribute"""
        self.request_Key = new_request_Key
        
    def get_100_art(self):
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
