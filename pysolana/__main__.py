from sol import *
from CopperUI import *
from sys import argv

def _airdrop(seed, ammount):
    ammount = ammount * 1000000000
    try:
        airdrop(seed, ammount)
    except Exception as e:
        return f"error: {e}"
    return f"airdropped {ammount/1000000000} to your wallet."

def main():
    clearscreen()
    banner("pysol")
    print("pysolana CLI airdrop tool.")
    prompt()
    clearscreen()
    banner("pysol")
    print("how many SOL would you like airdropped to your devnet wallet?")
    ammount = input(">> ")
    print("please enter your wallet address:")
    phrase = input(">> ")
    print("\nstarting airdrop...")
    print(_airdrop(phrase, ammount))

try:
    if argv[1] == "airdrop":
        main()
except IndexError:
    print("No args passed")
