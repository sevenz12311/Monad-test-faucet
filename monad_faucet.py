import requests
import time

# 你的钱包地址
wallet_address = "0xb796daB19e714Eaf48FDb2CaB2E1C5dD3ED9147f"

# 水龙头请求地址（假设的，需替换为真实 API）
faucet_url = "https://testnet.monad.xyz/api/claim"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}

data = {
    "address": wallet_address
}

def claim_tokens():
    response = requests.post(faucet_url, json=data, headers=headers)
    if response.status_code == 200:
        print("领取成功:", response.text)
    else:
        print("领取失败:", response.status_code, response.text)

claim_tokens()
