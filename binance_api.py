import requests
import pandas as pd


# DataFrame of crypto details
crypto=pd.DataFrame(data=None, columns=None)

 
# 
# get_crypto_details
# @Param: [Array] inputCrypto - Array of crypto symbols
# This function will get the details of the crypto symbols from the Binance API
# @Return: {Object} response_json - JSON object of crypto details
#
def get_crypto_details(inputCrypto):
    endpoint='['
    for i in range(n):
        endpoint = endpoint + '"'+inputCrypto[i]+'",'
    endpoint = endpoint[:-1] + ']'
    # print(endpoint)
    params = {'symbols': endpoint}
    try:
        url = 'https://api.binance.com/api/v3/exchangeInfo?'
        response = requests.get(url, params=params)
        response_json = response.json()["symbols"]
        response_to_df(response_json)
        return (response_json)
    except Exception as e:
        print(e)
        print('There was an error in the API call')
        return None

# 
# get_crypto_details
# @Param: [Array] inputCrypto
# This function will get the prices of the crypto symbols from the Binance API
# Adds Prices Column to crypto DataFrame
#

def get_crypto_price(inputCrypto):
    endpoint='['
    for i in range(n):
        endpoint = endpoint + '"'+inputCrypto[i]+'",'
    endpoint = endpoint[:-1] + ']'
    # print(endpoint)
    params = {'symbols': endpoint}
    try:

        url = 'https://api.binance.com/api/v3/ticker/price?'
        response = requests.get(url, params=params)
        response_json = response.json()
        prices=[]
        for i in response_json:
            prices.append(i["price"])
        global crypto
        crypto['price'] = prices

    except Exception as e:
        print(e)
        print('There was an error in the API call')
        return None
    
# 
# get_crypto_details
# @Param: [Array] inputCrypto
# Transform data to DataFrame
#

def response_to_df(response_json):
    if response_json is not None:
        df = pd.DataFrame(response_json)
        df = df[['symbol', 'status', 'baseAsset', 'quoteAsset']]
        global crypto
        crypto = df
        get_crypto_price(inputCrypto)
    else:
        print('No response data found')
        return None

# 
# convert_to_excel
# @Param: (string) filename
# Transform DataFrame to Excel with the inputted filename
#
def convert_to_excel(filename):
    global crypto
    crypto.to_excel(filename+'.xlsx', index=False)

# Input Crypto Array from User 
n = int(input("Enter the number of crypto currencies you want to check: "))
inputCrypto = []
for i in range(n):
    inputCrypto.append(input("Enter the crypto currency symbol eg.-BTCUSDT : "))

get_crypto_details(inputCrypto)

# Output
print(crypto)

# Convert to Excel
excel_name = input("Enter the name of the excel file: ")
convert_to_excel(excel_name)




