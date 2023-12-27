import requests
import os
from io import BytesIO
from zipfile import ZipFile

class Download:
    def __init__(self) -> None:
        self.remote_urls = ["https://www.fueleconomy.gov/feg/epadata/16data.zip", 
                            "https://www.fueleconomy.gov/feg/epadata/17data.zip", 
                            "https://www.fueleconomy.gov/feg/epadata/18data.zip", 
                            "https://www.fueleconomy.gov/feg/epadata/19data.zip", 
                            "https://www.fueleconomy.gov/feg/epadata/20data.zip",
                            "https://www.fueleconomy.gov/feg/epadata/21data.zip",
                            "https://www.fueleconomy.gov/feg/epadata/22data.zip",
                            "https://www.fueleconomy.gov/feg/epadata/23data.zip"]

        self.save()
        
    def save(self):
        # Make http request for remote file data
        for url in self.remote_urls:
            # Open url
            print('Downloading Started')
            data = requests.get(url)
            print('Downloading Completed')
            
            # Get the path of folder 'raw_data'
            path = os.path.abspath('raw_data') 
            
            # Extracting the zip file contents
            zipfile= ZipFile(BytesIO(data.content))
            
            # Save file data to local copy
            zipfile.extractall(path)
            
            # close zipfile we don't need
            zipfile.close()
            print('Raw Data Saved')
            
if __name__ == "__main__":
    a = Download()