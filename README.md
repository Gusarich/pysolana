# PySolana

PySolana is a Python library for dealing with Solana blockchain.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pysolana.

```bash
pip install pysolana
```

## Usage

There are 2 modules in `pysolana`:

 * `api.py` includes all RPC API Solana methods.
 * `sol.py` includes class `Sol` that used to simply manage Solana accounts with `Python3`

### api.py

You can see all RPC API Solana methods [here](https://docs.solana.com/apps/jsonrpc-api#json-rpc-api-reference)

Example:
```python
print(getTransactionCount()) # 555309062
```

### sol.py

#### Keypairs

To generate new keypair you need to create `Sol` object in code.
```python
keypair = Sol(chain='devnet')
print(keypair.seedphrase) # 12-words seedphrase that used to import keypair
print(keypair.pubkey) # Solana account address
```

To import keypair put seedphrase in `__init__` method.
```python
kp1 = Sol(chain='devnet')
kp2 = Sol(seedphrase=kp1.seedphrase, chain='testnet')
print(kp1.pubkey == kp2.pubkey) # True
```

One keypair can be used in different chains.

There are some methods in `Sol` class:
 * [set_chain](#setchain)
 * [balance](#balance)
 * [airdrop](#airdrop)
 * [transfer](#transfer)

#### set_chain
`set_chain(chain)` method used to change keypair chain.
```python
kp = Sol(chain='mainnet') # Created keypair

kp.balance() # Check balance in mainnet
kp.set_chain('testnet') # Set chain to testnet
kp.balance() # Check balance in testnet
```

#### balance
`balance()` method used to get balance of account.
```python
kp = Sol(seedphrase=my_seedphrase, chain='mainnet') # Created keypair

print(kp.balance()) # 15.0
```

#### airdrop
`aidrop(amount, wait=True)` method used to request airdrop of SOL tokens in devnet.
```python
kp = Sol(chain='devnet') # Created keypair

print(kp.balance()) # 0.0
kp.airdrop(100) # Request airdrop to account in devnet.
print(kp.balance()) # 100.0

kp.airdrop(100, wait=False)
# Here I can do anything without waiting transaction to confirm
print(kp.balance()) # 100.0
# Transaction is not confirmed in chain and balance() showing only confirmed balance.
```

#### transfer
`transfer(to, amount, wait=True)` method used to send SOL tokens to another account.
```python
kp1 = Sol(chain='devnet') # Created first keypair
kp2 = Sol(chain='devnet') # Created second keypair

kp1.airdrop(100)
kp2.airdrop(100)

print(kp1.balance()) # 100.0
print(kp2.balance()) # 100.0

kp1.transfer(kp2, 10) # 'to' can be Sol object or str pubkey

print(kp1.balance()) # 89.999995
print(kp2.balance()) # 110.0

kp2.transfer(kp1.pubkey, 10)

print(kp1.balance()) # 99.999995
print(kp2.balance()) # 99.999995

kp1.transfer(kp2, 50, wait=False)
# Here I can do anything without waiting transaction to confirm
print(kp1.balance()) # 99.999995
print(kp2.balance()) # 99.999995
# Transaction is not confirmed in chain and balance() showing only confirmed balance.
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
