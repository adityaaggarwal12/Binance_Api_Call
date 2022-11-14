import requests
import pandas as pd

# Array of crypto prices
prices=[]
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
    try:
        url = 'https://api.binance.com/api/v3/exchangeInfo?symbols='+endpoint
        response = requests.get(url)
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
    for n in inputCrypto:
        try:
            url = 'https://api.binance.com/api/v3/ticker/price?symbol='+n
            response = requests.get(url)
            response_json = response.json()

            global prices
            prices.append(response_json['price'])

            # print(response_json)
        except Exception as e:
            print(e)
            print('There was an error in the API call')
            return None
    global crypto
    crypto['price'] = prices

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
        # df.to_csv('crypto.csv', index=False)
    else:
        return None

# Input Crypto Array from User 
n = int(input("Enter the number of crypto currencies you want to check: "))
inputCrypto = []
for i in range(n):
    inputCrypto.append(input("Enter the crypto currency symbol eg.-BTCUSDT : "))

get_crypto_details(inputCrypto)
get_crypto_price(inputCrypto)


print(crypto)
