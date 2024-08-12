import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block", self.calculate_hash(0, "0", int(time.time()), "Genesis Block"))

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        if self.validate_block(new_block):
            self.chain.append(new_block)

    def validate_block(self, block):
        latest_block = self.get_latest_block()
        return (block.previous_hash == latest_block.hash and
                block.hash == self.calculate_hash(block.index, block.previous_hash, block.timestamp, block.data))

    def calculate_hash(self, index, previous_hash, timestamp, data):
        value = f"{index}{previous_hash}{timestamp}{data}"
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def proof_of_stake(self, data):
        latest_block = self.get_latest_block()
        index = latest_block.index + 1
        timestamp = int(time.time())
        previous_hash = latest_block.hash
        new_hash = self.calculate_hash(index, previous_hash, timestamp, data)
        new_block = Block(index, previous_hash, timestamp, data, new_hash)
        self.add_block(new_block)
        return new_block
def test_blockchain_with_merkle_tree():
    from blockchain.blockchain import Blockchain
    from blockchain.merkle_tree import merkle_tree

    blockchain = Blockchain()
    blockchain.proof_of_stake("Block 1 Data")
    blockchain.proof_of_stake("Block 2 Data")

    data_blocks = [block.data for block in blockchain.chain]
    merkle_root = merkle_tree(data_blocks)

    assert merkle_root is not None
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.proof_of_stake("Block 1 Data")
    blockchain.proof_of_stake("Block 2 Data")

    for block in blockchain.chain:
        print(f"Block {block.index}: {block.data} - Hash: {block.hash}")
