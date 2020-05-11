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
