# ----------------------------------------------------------- Libraries ----------------------------------------------------------- 

from collections import namedtuple
import hashlib
from datetime import datetime

# -------------------------------------------------------- Data Structures -------------------------------------------------------- 

Block = namedtuple('Block', ['id', 'hash', 'timestamp', 'data', 'previous_hash'])
Data = namedtuple('Data', ['sender', 'receiver', 'coins_id', 'value'])

# -------------------------------------------- Blockchain Creation and Genesis Block ---------------------------------------------- 

def create_blockchain():
    blockchain = []

    genesis_data = Data("System", "Satoshi", 0, 100)
    genesis_hash = generate_hash(1, datetime.now(), genesis_data, 0) 
    genesis_block = Block(1, genesis_hash, datetime.now(), genesis_data, 0)
    blockchain.append(genesis_block)

    return blockchain

# -------------------------------------------- Transaction and Block Creation Functions --------------------------------------------

def create_transaction(chain):
    sender = input("Enter the sender's name: ")
    receiver = input("Enter the receiver's name: ")
    coins_id = input("Enter the coin IDs (separated by commas): ").split(',')
    coins_id = [int(coin.strip()) for coin in coins_id]
    value = float(input("Enter the transaction value: "))

    while value <= 0:
        print("Value must be greater than 0.")
        value = float(input("Enter the transaction value: "))
       
    data = Data(sender, receiver, coins_id, value)
    timestamp = datetime.now()
    id = get_last_block(chain).id + 1
    previous_hash = get_last_block(chain).hash
    
    hash = generate_hash(id, timestamp, data, previous_hash)
    return Block(id, hash, timestamp, data, previous_hash)

def add_block(chain, block):
    if validate_transaction(chain, block):
        print("The block was validated and added to the blockchain!")
        chain.append(block)
    else:
        print("Please review your information. Something went wrong!")

# ------------------------------------------ Helper Functions for Hashing and Validation -------------------------------------------

def get_last_block(chain):
    return chain[-1]

def generate_hash(id, timestamp, data, previous_hash):
    block_data = f"{id}{timestamp}{data}{previous_hash}".encode()
    return hashlib.sha256(block_data).hexdigest()

def validate_transaction(chain, block):
    total = 0
    for element in chain:
        if element.data.receiver == block.data.sender:
            total += element.data.value
        if element.data.sender == block.data.sender:
            total -= element.data.value
    
    if block.data.value <= total and validate_coin_ownership(chain, block):
        return True
    else:
        return False

def validate_coin_ownership(chain, block):
    owned_coins = set()
    
    for element in chain:
        if element.data.receiver == block.data.sender:
            owned_coins.add(element.id)
        if element.data.sender == block.data.sender:
            owned_coins.discard(element.id)

    return all(coin in owned_coins for coin in block.data.coins_id)

def validate_blockchain(chain):

    for index in range(1,len(chain)): 
        current_block = chain[index]
        previous_block = chain[index - 1]
        
        if current_block.previous_hash != previous_block.hash:
            print(f"Hash mismatch: The hash of the previous block (ID = {previous_block.id}) does not match the stored previousHash in the current block (ID = {current_block.id}).")
            return False
        
        expected_hash = generate_hash(current_block.id, current_block.timestamp, current_block.data, current_block.previous_hash)
        if current_block.hash != expected_hash:
            print(f"Invalid hash: The current block's hash (ID = {current_block.id}) is incorrect and does not match the expected value.")
            return False

    return True

# ------------------------------------------ Blockchain and Block Display Functions ------------------------------------------------

def show_block(block):
    print("+" + "-" * 96 + "+")
    print(f"| {'ID: ' + str(block.id):^94} |")
    print("+" + "-" * 96 + "+")
    print(f"| {'Hash: ' + str(block.hash):^94} |")
    print("+" + "-" * 96 + "+")
    print(f"| {'Timestamp: ' + block.timestamp.strftime('%Y-%m-%d %H:%M:%S'):^94} |")
    print("+" + "-" * 96 + "+")
    print(f"| {'Previous Hash: ' + str(block.previous_hash):^94} |")
    print("+" + "-" * 96 + "+")
    print("|                Sender                |               Receiver               |       Value      |")
    print("+" + "-" * 96 + "+")
    print(f"|{block.data.sender:^38}|{block.data.receiver:^38}|{block.data.value:^18}|")
    print("+" + "-" * 96 + "+ \n")
    
def show_chain(chain):
    for block in chain:
        show_block(block)

# ---------------------------------------------------------- Main Program ----------------------------------------------------------

blockchain = create_blockchain()

while True:
    print("\nOptions Menu:")
    print("1. Add a new block")
    print("2. Display the blockchain")
    print("3. Validate the blockchain")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        block = create_transaction(blockchain)
        add_block(blockchain,  block)
    
    elif choice == "2":
        print("\nDisplaying the complete blockchain:")
        show_chain(blockchain)
    
    elif choice == "3":
        if validate_blockchain(blockchain):
            print("\nThe blockchain is valid!")
        else:
            print("\nThe blockchain has been compromised!")
    
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option!")