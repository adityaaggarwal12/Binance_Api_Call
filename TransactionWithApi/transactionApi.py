import hmac
import hashlib
import requests  
from decouple import config



secret_key = bytes(config('SECRET_KEY'),'utf-8')
api_key = bytes(config('API_KEY'),'utf-8')

def get_ts():
    res = requests.get("https://api.binance.com/api/v3/time")
    ts=str(res.json()["serverTime"])
    return ts

def get_HMAC(params,secretKey):
    paramsB = bytes(params,'utf-8')
    signature = hmac.new(secretKey, paramsB, hashlib.sha256).hexdigest()
    return format(signature)

headers = {'X-MBX-APIKEY' : api_key}
ts=get_ts()

total_params = "symbol=BTCUSDT&side=SELL&type=MARKET&quantity=0.01&recvWindow=5000&timestamp="+ts

signature=get_HMAC(total_params,secret_key)

def exec_transaction():
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


# try:
#     url_base = 'https://testnet.binance.vision/api/v3/order?'
#     req_url = url_base+total_params+"&signature="+signature
#     response = requests.post(req_url,headers=headers)
#     response_json = response.json()
#     print(response_json)
# except Exception as e:
#     print(e)
#     print('There was an error in the API call')

