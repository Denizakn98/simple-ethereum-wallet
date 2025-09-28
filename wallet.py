import os
from web3 import Web3
from eth_account import Account

# Set your Infura or node endpoint here
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_PROJECT_ID"
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

def generate_wallet():
    acct = Account.create()
    print("Address:", acct.address)
    print("Private Key:", acct.key.hex())

def check_balance(address):
    balance = w3.eth.get_balance(address)
    print(f"Balance of {address}: {w3.fromWei(balance, 'ether')} ETH")

def send_eth(private_key, to_address, amount_eth):
    acct = Account.from_key(private_key)
    nonce = w3.eth.get_transaction_count(acct.address)
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': w3.toWei(amount_eth, 'ether'),
        'gas': 21000,
        'gasPrice': w3.toWei('20', 'gwei'),
    }
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Transaction sent! Hash:", tx_hash.hex())

def main():
    print("Simple Ethereum Wallet")
    print("1. Generate Wallet")
    print("2. Check Balance")
    print("3. Send ETH")
    choice = input("Choose option: ")
    if choice == '1':
        generate_wallet()
    elif choice == '2':
        addr = input("Enter address: ")
        check_balance(addr)
    elif choice == '3':
        pk = input("Enter your private key: ")
        to = input("Send to address: ")
        amt = float(input("Amount in ETH: "))
        send_eth(pk, to, amt)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
