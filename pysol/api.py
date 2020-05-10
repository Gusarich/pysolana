import requests
import json


CHAINS = {
    'mainnet': 'https://api.mainnet-beta.solana.com',
    'testnet': 'https://testnet.solana.com',
    'devnet': 'https://devnet.solana.com'
}


def call(method, chain, params=None):
    url = CHAINS[chain]
    headers = {'Content-Type': 'application/json'}
    if params:
        data = json.dumps({'jsonrpc': '2.0',
                           'id': 1,
                           'method': method,
                           'params': params})
    else:
        data = json.dumps({'jsonrpc': '2.0',
                           'id': 1,
                           'method': method})

    response = requests.post(url, headers=headers, data=data)

    return response


def getTransactionCount(chain='mainnet'):
    response = call('getTransactionCount', chain)
    if response:
        data = json.loads(response.text)
        return int(data['result'])
    else:
        return False
