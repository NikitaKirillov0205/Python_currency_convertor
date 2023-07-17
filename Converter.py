import requests

url = "http://data.fixer.io/api/latest?access_key=e7ae7a8249eb1e32898ba86eb2eb575d"
params = {
    "apikey": "e7ae7a8249eb1e32898ba86eb2eb575d"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
else:
    print("Request failed with status code:", response.status_code)

while True:
    a = input("Do you want to quit or convert?\n")
    if a == 'quit':
        exit()
    if a == 'convert':
        a = input("What currency do you want to convert? (Options: EUR GBP USD CHF JPY)\n")
        if a == 'USD':
            currency1 = 'USD'
        elif a == 'EUR':
            currency1 = 'EUR'
        elif a == 'GBP':
            currency1 = 'GBP'
        elif a == 'JPY':
            currency1 = 'JPY'
        elif a == 'CHF':
            currency1 = 'CHF'
        else:
            print("There is no such currency, try again")
            pass
        a = input('What currency do you want to convert to?\n')
        if a == 'USD':
            currency2 = 'USD'
        elif a == 'EUR':
            currency2 = 'EUR'
        elif a == 'GBP':
            currency2 = 'GBP'
        elif a == 'JPY':
            currency2 = 'JPY'
        elif a == 'CHF':
            currency2 = 'CHF'
        else:
            print("There is no such currency, try again")
            pass
        try:
            amount = float(input('What amount would you like to convert? (Use ONLY numbers)\n'))
        except:
            print('ERROR Try again')
            exit()
        Converted_amount = amount * data['rates'][currency1] * data['rates'][currency2]
        print(f'{Converted_amount} {currency2} - this is converted amount')
    else:
        pass
