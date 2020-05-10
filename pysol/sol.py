from subprocess import Popen, check_output, PIPE


CHAINS = {
    'mainnet': 'https://api.mainnet-beta.solana.com',
    'testnet': 'https://testnet.solana.com',
    'devnet': 'https://devnet.solana.com'
}


class Sol:
    def __init__(self, seedphrase=None, chain='mainnet'):
        if seedphrase:
            self.seedphrase = seedphrase
            self.pubkey = check_output(f'printf "{self.seedphrase}\n\n" | ' +\
                                       'solana-keygen pubkey ASK',
                                       shell=True, stderr=PIPE).decode()
        else:
            p = Popen('solana-keygen new --no-outfile --no-passphrase',
                      shell=True, stderr=PIPE)

            text = p.stderr.read().decode().split('\n')

            self.pubkey = text[1][8:]
            self.seedphrase = text[4]

    def setChain(self, chain):
        self.chain = chain

    def balance(self):
        return check_output(f'solana balance {self.pubkey}' +\
                            f'--url {CHAINS[self.chain]}',
                            shell=True).decode()[:-5]

    def transfer(self, to, amount):
        return check_output(f'printf "{self.seedphrase}\n\n{self.seedphrase}' +\
                            '\n\n" | solana transfer --no-wait --fee-payer' +\
                            f'ASK --from ASK {to} {amount}' +\
                            f'--url {CHAINS[self.chain]}',
                            shell=True, stderr=PIPE).decode()
