# Run : $ python3 -m app.scripts.client
import requests

def get_country_details(country):
    url = f"http://192.168.1.100:5000/countries/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()
    
def main():
    print(get_country_details(input("Enter the country name: ")))
 
if __name__ == "__main__":
    main()
