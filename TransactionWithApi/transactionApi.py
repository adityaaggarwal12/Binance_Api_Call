import hmac
import hashlib
import requests  
from decouple import config


secret_key = bytes(config('SECRET_KEY'),'utf-8')
api_key = bytes(config('API_KEY'),'utf-8')

#
# get_ts() \
# returns the server time in milliseconds
#
def get_ts():
    res = requests.get("https://api.binance.com/api/v3/time")
    ts=str(res.json()["serverTime"])
    return ts
#
# get_account_balance
# @Param: [String] params , [byte encoded] secret_key
# This function will produce hmac sha256 signature
# @Return: {String} signature - hmac sha256 signature
#
def get_HMAC(params,secretKey):
    paramsB = bytes(params,'utf-8')
    signature = hmac.new(secretKey, paramsB, hashlib.sha256).hexdigest()
    return format(signature)

ts=get_ts()

total_params = "symbol=BTCUSDT&side=BUY&type=MARKET&quantity=0.1&recvWindow=5000&timestamp="+ts

#
# get_account_balance
# @Param: [object] headers , [string] signature
# This function will execute the transaction on Binance 
# @Return: {Object} response_json - JSON object of transaction details
#
def exec_transaction(headers,signature):
    try:
#        url_base = 'https://api.binance.com/api/v3/order?
        url_base = 'https://testnet.binance.vision/api/v3/order?'
        req_url = url_base+total_params+"&signature="+signature
        response = requests.post(req_url,headers=headers)
        response_json = response.json()
        print(response_json)

        return (response_json)
    except Exception as e:
        print(e)
        print('There was an error in the API call')
        return None


signature=get_HMAC(total_params,secret_key)
headers = {
    'X-MBX-APIKEY' : api_key
}

exec_transaction(headers,signature)
