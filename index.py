# Do not use this code for illegal or dangerous purposes. I am not responsible for what you do with it.

import time
from web3 import Web3
from mnemonic import Mnemonic

def write_data(address, seed):
    with open("./data/data_without.txt", "a") as file:
        file.write(f"{address}  -  {seed}\n")

def write_complete(address, seed):
    with open("./data/data_found.txt", "a") as file:
        file.write(f"{address}  -  {seed}\n")

def check_balance():
    """
    Generates an EVM-compatible 12 or 24 word sentence, extracts the associated address and checks its balance.
    And if the address contains ETH, adds it to the list of addresses with funds and its seed phrase.
    """
    
    global total_found  # Indicate that you are using the global variable

    # Generate an EVM-compatible 12-word sentence
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(128)

    # Extract the private key and public address from these 12 words
    seed = Mnemonic.to_seed(mnemonic_phrase)
    private_key = seed[:32]
    account = w3.eth.account.from_key(private_key)
    address = account.address

    # Check if this address has cryptocurrency
    balance = w3.eth.get_balance(address)
    eth_balance = w3.from_wei(balance, 'ether')

    # If it has any, return the result to the console and store the mnemonic phrase
    if eth_balance > 0:
        total_found += eth_balance
        print(f"Fund found in: {address} with {eth_balance}ETH its seedphrase is - ", mnemonic_phrase)
        write_complete(address, mnemonic_phrase)
    else:
        print(f"Not fund found in {address}  -  ETH total found : {total_found}ETH")
        write_data(address, mnemonic_phrase)

# Variable to track total cryptocurrencies found
total_found = 0

# List to store seed phrases with funds (If you want to keep this)
seed_with_funds = []
# List to store addresses with funds (If you want to keep this)
addresses_with_funds = []

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/XXXXXXXXXXX'))

if __name__ == "__main__":
    try:
        # Continuously check for balances
        while True:
            check_balance()
            time.sleep(0.9)  # Spreading 100,000 free Infura queries (0.9 default).
    except Exception as e:
        print(f"An error occurred: {e}")

# Code by: Kirno