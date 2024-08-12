import hashlib

def hash_function(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def merkle_tree(data_blocks):
    if len(data_blocks) == 1:
        return data_blocks[0]
    
    new_level = []
    for i in range(0, len(data_blocks) - 1, 2):
        new_hash = hash_function(data_blocks[i] + data_blocks[i + 1])
        new_level.append(new_hash)

    if len(data_blocks) % 2 == 1:
        last_hash = hash_function(data_blocks[-1] + data_blocks[-1])
        new_level.append(last_hash)

    return merkle_tree(new_level)
if __name__ == "__main__":
    data_blocks = ["block1", "block2", "block3", "block4"]
    merkle_root = merkle_tree(data_blocks)
    print(f"Merkle Root: {merkle_root}")
