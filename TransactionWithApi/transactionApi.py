import hmac
import hashlib
import requests  
from decouple import config


secret_key = bytes(config('SECRET_KEY'),'utf-8')
api_key = bytes(config('API_KEY'),'utf-8')

#
# get_ts() 
# returns the server time in milliseconds
#
def get_ts():
    res = requests.get("https://api.binance.com/api/v3/time")
    ts=str(res.json()["serverTime"])
    return ts


#
# get_account_balance
# @Param: [object] params , [byte encoded] secret_key
# This function will produce hmac sha256 signature
# @Return: {String} signature - hmac sha256 signature
#
def get_HMAC(params,secretKey):
    newParams =""

    for i in params.keys():
        newParams = newParams + i + "=" + params[i] + "&"
    newParams = newParams[:-1]

    paramsB = bytes(newParams,'utf-8')
    signature = hmac.new(secretKey, paramsB, hashlib.sha256).hexdigest()
    return format(signature)




#
# get_account_balance
# @Param: [object] headers , [string] signature
# This function will execute the transaction on Binance 
# @Return: {Object} response_json - JSON object of transaction details
#
def exec_transaction(params,headers):
    try:
#        url_base = 'https://api.binance.com/api/v3/order?
        url_base = 'https://testnet.binance.vision/api/v3/order?'
        # req_url = url_base+total_params+"&signature="+signature
        response = requests.post(url_base,headers=headers,params=params)
        response_json = response.json()
        print(response_json)

        return (response_json)
    except Exception as e:
        print(e)
        print('There was an error in the API call')
        return None

symbol = input("enter the symbol ex BTCUSDT:")
side = input("enter the side - BUY/SELL:")
type = input("enter the type ex MARKET/LIMIT:")
quantity = input("enter the quantity:")

params = {
    "symbol": symbol,
    "side": side,
    "type": type,
    "quantity": quantity,
    "recvWindow": "5000",
}
if(type=="LIMIT"):
    price = input("enter the price:")
    params["price"] = price

ts=get_ts()
params["timestamp"] = ts


signature=get_HMAC(params,secret_key)
headers = {
    'X-MBX-APIKEY' : api_key
}

params["signature"] = signature


exec_transaction(params,headers)
