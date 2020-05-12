# PySolana

PySolana is a Python library for dealing with Solana blockchain.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pysolana.

```bash
pip3 install pysolana
```

## Usage

There are 2 modules in `pysolana`:

 * `api` includes all RPC API Solana methods.
 * `sol` includes class `Sol` that used to simply manage Solana accounts with `Python3`

### api

You can see all RPC API Solana methods [here](https://docs.solana.com/apps/jsonrpc-api#json-rpc-api-reference). Every method from RPC API writen to function in `api` module.

Example:
```python
from pysolana.api import *

print(getTransactionCount()) # 555309062
```

### sol

#### Keypairs

To generate new keypair you need to create `Sol` object in code.
```python
from pysolana.sol import *

keypair = Sol(chain='devnet')
print(keypair.seedphrase) # 12-words seedphrase that used to import keypair
print(keypair.pubkey) # Solana account address
```

To import keypair put seedphrase in `__init__` method.
```python
from pysolana.sol import *

kp1 = Sol(chain='devnet')
kp2 = Sol(seedphrase=kp1.seedphrase, chain='testnet')
print(kp1.pubkey == kp2.pubkey) # True
```

One keypair can be used in different chains.

There are some methods in `Sol` class:
 * [set_chain](#set_chain)
 * [balance](#balance)
 * [airdrop](#airdrop)
 * [transfer](#transfer)
 * [create_stake_account](#create_stake_account)
 * [delegate_stake](#delegate_stake)
 * [deactivate_stake](#deactivate_stake)
 * [withdraw_stake](#withdraw_stake)

#### set_chain
`set_chain(chain)` method used to change keypair chain.
```python
from pysolana.sol import *

kp = Sol(chain='mainnet') # Created keypair

kp.balance() # Check balance in mainnet
kp.set_chain('testnet') # Set chain to testnet
kp.balance() # Check balance in testnet
```

#### balance
`balance()` method used to get balance of account.
```python
from pysolana.sol import *

kp = Sol(seedphrase=my_seedphrase, chain='mainnet') # Created keypair

print(kp.balance()) # 15.0
```

#### airdrop
`aidrop(amount, wait=True)` method used to request airdrop of SOL tokens in devnet.
```python
from pysolana.sol import *

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
from pysolana.sol import *

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

#### create_stake_account
`create_stake_account(amount)` method used to create new stake account.
```python
from pysolana.sol import *

kp = Sol(chain='devnet') # Create new keypair
kp.airdrop(200)

stake_account = kp.create_stake_account(100) # Creating new stake account
print(stake_account) # Dhyi75k1aA4Rfn99gh4XCT64yxvGzCpu81ZE4iDe3RZz
print(kp.balance()) # 99.99999
```

#### delegate_stake
`delegate_stake(stake_account, vote_account)` method used to delegate stake at account `stake_account` for validator `vote_account`.
```python
from pysolana.sol import *

kp = Sol(chain='devnet') # Create new keypair
kp.airdrop(1000)

stake_account = kp.create_stake_account(100) # Creating new stake account

kp.delegate_stake(stake_account, '5MMCR4NbTZqjthjLGywmeT66iwE9J9f7kjtxzJjwfUx2') # Delegating ALL stake to validator
```

#### deactivate_stake
`deactivate_stake(stake_account)` method used to deactivate stake from `stake_account`
```python
from pysolana.sol import *

kp = Sol(chain='devnet') # Create new keypair
kp.airdrop(1000)

stake_account = kp.create_stake_account(100) # Creating new stake account with 100 SOL staked

kp.delegate_stake(stake_account, '5MMCR4NbTZqjthjLGywmeT66iwE9J9f7kjtxzJjwfUx2') # Delegating ALL stake to validator

print(kp.balance()) # 899.999985
kp.deactivate_stake(stake_account) # Deactivating ALL stake from stake_account
# Stake transactions take some time to proceed in blockchain, so you need to wait until your SOL tokens back to account

# Some time later:
print(kp.balance()) # 999.99998
```

#### withdraw_stake
`withdraw_stake(stake_account, amount)` method used to withdraw stake dividends from `stake_account`
```python
from pysolana.sol import *

kp = Sol(chain='devnet') # Create new keypair
kp.airdrop(1000)

stake_account = kp.create_stake_account(100) # Creating new stake account with 100 SOL staked

kp.delegate_stake(stake_account, '5MMCR4NbTZqjthjLGywmeT66iwE9J9f7kjtxzJjwfUx2') # Delegating ALL stake to validator

print(kp.balance()) # 899.999985

# Some time later:
kp.withdraw_stake(stake_account, 3)
print(kp.balance()) # 902.99998
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
