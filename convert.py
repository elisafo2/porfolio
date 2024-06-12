import requests

API_KEY = 'f7bdfe197faa50ad9203148c'
API_url = f'https://v6.exchangerate-api.com/v6/f7bdfe197faa50ad9203148c/latest/USD'

print("Hello! Welcome to the US/South African currency converter. This can be used to convert USD to ZAR and ZAR to USD")
def get_exchange_rate():
    response = requests.get(API_url)
    data = response.json()
    if data['result'] == "success":
        return data["conversion_rates"]["ZAR"]
    else:
        raise Exception("Error")

def get_exchange_rate2():
    response = requests.get(API_url)
    data = response.json()
    if data['result'] == "sucess":
        return data["conversion_rates"]["USD"]
    else:
        raise Exception("Error")

def convert_usd_to_zar(usd_amount):
    rate = get_exchange_rate()
    return usd_amount * rate

def convert_zar_to_usd(zar_amount):
    rate2 = get_excahnge_rate2()
    return zar_amount * rate2

if __name__ == "__main__":
    usd_amount = float(input("Enter amount in USD here: " ))
    zar_amount = convert_usd_to_zar(usd_amount)
    print(f"{usd_amount} USD is equal to {zar_amount:.2f} ZAR")
    zar_amount = float(input("Enter amount in ZAR here: "))
    print(f"{zar_amount} ZAR is equal to {usd_amount:.2f} USD")
    
