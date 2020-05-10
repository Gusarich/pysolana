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


def getAccountInfo(pubkey, chain='mainnet'):
    response = call('getAccountInfo', chain, [pubkey])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getBalance(pubkey, chain='mainnet'):
    response = call('getBalance', chain, [pubkey])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getBlockCommitment(slot, chain='mainnet'):
    response = call('getBlockCommitment', chain, [slot])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getBlockTime(slot, chain='mainnet'):
    response = call('getBlockTime', chain, [slot])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getClusterNodes(chain='mainnet'):
    response = call('getClusterNodes', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getConfirmedBlock(slot, chain='mainnet'):
    response = call('getConfirmedBlock', chain, [slot])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getConfirmedBlocks(start_slot, end_slot=None, chain='mainnet'):
    if end_slot:
        response = call('getConfirmedBlocks', chain, [start_slot, end_slot])
    else:
        response = call('getConfirmedBlocks', chain, [start_slot])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getConfirmedSignaturesForAddress(pubkey, start_slot,
                                     end_slot, chain='mainnet'):
    response = call('getConfirmedSignaturesForAddress', chain,
                    [pubkey, start_slot, end_slot])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getConfirmedTransaction(signature, chain='mainnet'):
    response = call('getConfirmedTransaction', chain, [signature])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getEpochInfo(chain='mainnet'):
    response = call('getEpochInfo', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getEpochSchedule(chain='mainnet'):
    response = call('getEpochSchedule', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getFeeCalculatorForBlockhash(blockhash, chain='mainnet'):
    response = call('getFeeCalculatorForBlockhash', chain, [blockhash])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getFeeRateGovernor(chain='mainnet'):
    response = call('getFeeRateGovernor', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getFirstAvailableBlock(chain='mainnet'):
    response = call('getFirstAvailableBlock', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getGenesisHash(chain='mainnet'):
    response = call('getGenesisHash', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getIdentity(chain='mainnet'):
    response = call('getIdentity', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getInflation(chain='mainnet'):
    response = call('getInflation', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getLargestAccounts(chain='mainnet'):
    response = call('getLargestAccounts', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getLeaderSchedule(slot=None, chain='mainnet'):
    if slot:
        response = call('getLeaderSchedule', chain, [slot])
    else:
        response = call('getLeaderSchedule', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getMinimumBalanceForRentExemption(datalenght, chain='mainnet'):
    response = call('getMinimumBalanceForRentExemption', chain, [datalenght])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getProgramAccounts(pubkey, chain='mainnet'):
    response = call('getProgramAccounts', chain, [pubkey])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getRecentBlockhash(chain='mainnet'):
    response = call('getRecentBlockhash', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getSignatureStatuses(signatures, chain='mainnet'):
    response = call('getSignatureStatuses', chain, [signatures])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getSlot(chain='mainnet'):
    response = call('getSlot', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getSlotLeader(chain='mainnet'):
    response = call('getSlotLeader', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getSlotsPerSegment(chain='mainnet'):
    response = call('getSlotsPerSegment', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getStoragePubkeysForSlot(chain='mainnet'):
    response = call('getStoragePubkeysForSlot', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getStorageTurn(chain='mainnet'):
    response = call('getStorageTurn', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getStorageTurnRate(chain='mainnet'):
    response = call('getStorageTurnRate', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getTransactionCount(chain='mainnet'):
    response = call('getTransactionCount', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getTotalSupply(chain='mainnet'):
    response = call('getTotalSupply', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getVersion(chain='mainnet'):
    response = call('getVersion', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def getVoteAccounts(chain='mainnet'):
    response = call('getVoteAccounts', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def minimumLedgerSlot(chain='mainnet'):
    response = call('minimumLedgerSlot', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def requestAirdrop(pubkey, lamports, chain='mainnet'):
    response = call('requestAirdrop', chain, [pubkey, lamports])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def sendTransaction(signedtx, chain='mainnet'):
    response = call('sendTransaction', chain, [signedtx])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def setLogFilter(logfilter, chain='mainnet'):
    response = call('setLogFilter', chain, [logfilter])
    if response:
        data = response.json()
        return data['result']
    else:
        return False


def validatorExit(chain='mainnet'):
    response = call('validatorExit', chain)
    if response:
        data = response.json()
        return data['result']
    else:
        return False
