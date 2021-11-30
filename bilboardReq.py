# This module imports data given by user
import requests

# Opening local file containing a auth key so i dont have to type it each time
with open('requestKey.txt') as f:
    local_Req_Key = f.readline()

class Bilboard:
    def __init__(self, range="10", date="2019-05-11", request_Key=local_Req_Key):
        self.art_Url = 'https://billboard-api2.p.rapidapi.com/artist-100'
        self.bil_Url = 'https://billboard-api2.p.rapidapi.com/hot-100'
        self.range = range
        self.date = date
        self.request_Key = request_Key
    
    #Setters
    def set_range(self, new_range):
        """Setter for range attribute"""
        self.range = new_range

    def set_date(self, new_date):
        """Setter for date attribute"""
        self.date = new_date
        
    def set_request_Key(self, new_request_Key):
        """Setter for request_Key attribute"""
        self.request_Key = new_request_Key
    
    #Getters
    def get_range(self):
        """Getter for range attribute"""
        return self.range
    
    def get_date(self):
        """Getter for date attribute"""
        return self.date
    
    def get_request_Key(self):
        """Getter for request_Key attribute"""
        return self.request_Keys
    
    #Getting bilboard and artist data
    def get_100_art(self):
        """request This function requests top100 artists data"""

        # format of a request
        querystring = {"range": f"1-{self.range}", "date": "2019-05-11"}

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

    #String method
    def __str__(self):
        """Prints attributes of current Bilboard class"""
        return f'Bibloard({self.range}, {self.date}, {self.request_Key})'