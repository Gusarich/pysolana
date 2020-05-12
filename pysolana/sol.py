from subprocess import Popen, call, check_output, PIPE, CalledProcessError


CHAINS = {
    'mainnet': 'https://api.mainnet-beta.solana.com',
    'testnet': 'https://testnet.solana.com',
    'devnet': 'https://devnet.solana.com'
}


class Sol:
    def __init__(self, seedphrase=None, chain='mainnet'):
        if seedphrase:
            self.seedphrase = seedphrase
            try:
                self.pubkey = check_output(f'printf "{self.seedphrase}\n\n" ' +\
                                           '| solana-keygen pubkey ASK',
                                           shell=True, stderr=PIPE).decode()\
                                           [:-1]
                error = False
            except CalledProcessError as grepexc:
                error = True
            if error:
                raise Exception('keygen error')
        else:
            p = Popen('solana-keygen new --no-outfile --no-passphrase',
                      shell=True, stderr=PIPE)

            text = p.stderr.read().decode().split('\n')

            self.pubkey = text[1][8:]
            self.seedphrase = text[4]

        self.chain = chain

    def set_chain(self, chain):
        self.chain = chain

    def balance(self):
        try:
            return float(check_output(f'solana balance {self.pubkey} ' +\
                            f'--url {CHAINS[self.chain]}',
                            shell=True).decode()[:-5])
        except CalledProcessError as grepexc:
            pass
        raise Exception('balance error')

    def airdrop(self, amount, wait=True):
        if self.chain != 'devnet':
            raise Exception('airdrop is not allowed in this chain')

        if wait:
            call(f'solana airdrop {amount} {self.pubkey} ' +\
                  f'--url {CHAINS[self.chain]}',
                  shell=True, stdout=PIPE, stderr=PIPE)

        else:
            Popen(f'solana airdrop {amount} {self.pubkey} ' +\
                  f'--url {CHAINS[self.chain]}',
                  shell=True, stdout=PIPE, stderr=PIPE)

    def transfer(self, to, amount, wait=True):
        if to.__class__.__name__ == 'Sol':
            to = to.pubkey

        if wait:
            text = f'printf "{self.seedphrase}\n\n{self.seedphrase}' +\
                   '\n\n" | solana transfer --fee-payer ' +\
                   f'ASK --from ASK {to} {amount} ' +\
                   f'--url {CHAINS[self.chain]}'
        else:
            text = f'printf "{self.seedphrase}\n\n{self.seedphrase}' +\
                   '\n\n" | solana transfer --no-wait --fee-payer ' +\
                   f'ASK --from ASK {to} {amount} ' +\
                   f'--url {CHAINS[self.chain]}'

        try:
            return check_output(text, shell=True, stderr=PIPE).decode()[:-1]
        except CalledProcessError as grepexc:
            pass
        raise Exception('transfer error')

    def create_stake_account(self, amount):
        stake_account = Sol()
        text = f'printf "{self.seedphrase}\n\n{self.seedphrase}\n\n' +\
               f'{self.seedphrase}\n\n{self.seedphrase}\n\n' +\
               f'{stake_account.seedphrase}" | ' +\
               'solana create-stake-account --from ASK ASK 100' +\
               ' --stake-authority ASK --withdraw-authority ASK --fee-payer ASK'
        call(text, shell=True, stdout=PIPE, stderr=PIPE)
        try:
            return stake_account.pubkey
        except CalledProcessError as grepexc:
            pass
        raise Exception('stake account error')

    def delegate_stake(self, stake_account, vote_account):
        text = f'printf "{self.seedphrase}\n\n{self.seedphrase}\n\n" | ' +\
               f'solana delegate-stake {stake_account} {vote_account} ' +\
               '--stake-authority ASK --fee-payer ASK'

        try:
            call(text, shell=True, stdout=PIPE, stderr=PIPE)
            error = False
        except CalledProcessError as grepexc:
            error = True
        if error:
            raise Exception('delegate stake error')

    def deactivate_stake(self, stake_account):
        text = f'printf "{self.seedphrase}\n\n{self.seedphrase}\n\n" | ' +\
               f'solana deactivate-stake {stake_account} ' +\
               '--stake-authority ASK --fee-payer ASK'

        try:
            call(text, shell=True, stdout=PIPE, stderr=PIPE)
            error = False
        except CalledProcessError as grepexc:
            error = True
        if error:
            raise Exception('deactivate stake error')

    def withdraw_stake(self, stake_account, amount):
        text = f'printf "{self.seedphrase}\n\n{self.seedphrase}\n\n" | ' +\
               f'solana withdraw-stake {stake_account} {self.pubkey}' +\
               f' {amount} --withdraw-authority ASK --fee-payer ASK'

        try:
            call(text, shell=True)
            error = False
        except CalledProcessError as grepexc:
            error = True
        if error:
            raise Exception('withdraw stake error')



kp = Sol(chain='devnet') # Create new keypair
kp.airdrop(1000)

stake_account = kp.create_stake_account(100) # Creating new stake account with 100 SOL staked

kp.delegate_stake(stake_account, '5MMCR4NbTZqjthjLGywmeT66iwE9J9f7kjtxzJjwfUx2') # Delegating ALL stake to validator

print(kp.balance()) #
kp.deactivate_stake(stake_account) # Deactivating ALL stake from stake_account
# It takes some time to proceed this type of transactions, so you need to wait until you get your SOL back to main account.

# Some time later:
print(kp.balance())
