import hashlib
import math
def hash_function(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def merkle_tree_optimized(data_blocks):
    """
    Construct an optimized Merkle Tree from the list of data blocks.
    
    Parameters:
        data_blocks (list): List of data blocks to be hashed.
    
    Returns:
        str: The Merkle Root of the tree.
    """
    if len(data_blocks) == 0:
        return None
    if len(data_blocks) == 1:
        return hash_function(data_blocks[0])
    
    new_level = []
    for i in range(0, len(data_blocks), 2):
        if i + 1 < len(data_blocks):
            combined_hash = hash_function(data_blocks[i] + data_blocks[i + 1])
        else:
            combined_hash = hash_function(data_blocks[i] + data_blocks[i])
        new_level.append(combined_hash)
    
    # Recursively build the tree
    return merkle_tree_optimized(new_level) if len(new_level) > 1 else new_level[0]

def validate_merkle_proof(proof, root, leaf):
    """
    Validate a Merkle proof against a known root.
    
    Parameters:
        proof (list): List of sibling hashes leading to the root.
        root (str): The Merkle root.
        leaf (str): The leaf node hash to validate.
    
    Returns:
        bool: True if the proof is valid, False otherwise.
    """
    current_hash = hash_function(leaf)
    for sibling_hash in proof:
        current_hash = hash_function(current_hash + sibling_hash)
    return current_hash == root