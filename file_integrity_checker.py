import hashlib
import os
import json
import xxhash
import logging
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(filename='file_integrity.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to calculate the hash of a file using xxhash
def calculate_file_hash(file_path):
    """Calculate the hash of a file using xxhash."""
    hasher = xxhash.xxh64()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None

# Function to load stored hashes from a file
def load_hashes(hash_file='file_hashes.json'):
    """Load stored file hashes from a JSON file."""
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            return json.load(f)
    return {}

# Function to save hashes to a file
def save_hashes(hashes, hash_file='file_hashes.json'):
    """Save file hashes to a JSON file."""
    with open(hash_file, 'w') as f:
        json.dump(hashes, f, indent=4)

# Function to monitor file integrity
def monitor_file_integrity(file_path, hash_file='file_hashes.json'):
    """Monitor changes in a file by comparing its hash to a stored value."""
    hashes = load_hashes(hash_file)
    current_hash = calculate_file_hash(file_path)
    if current_hash is None:
        return
    
    if file_path in hashes:
        stored_hash = hashes[file_path]
        if stored_hash == current_hash:
            logging.info(f"No changes detected in file: {file_path}")
        else:
            logging.warning(f"File modified: {file_path}")
            logging.warning(f"Stored hash: {stored_hash}")
            logging.warning(f"Current hash: {current_hash}")
    else:
        logging.info(f"New file added for monitoring: {file_path}")
    
    # Update stored hash
    hashes[file_path] = current_hash
    save_hashes(hashes, hash_file)

# Main function to run the file integrity checker
def main():
    files_to_monitor = ['example_file.txt']  # Modify this list as needed
    
    # Run integrity checks in parallel
    with ThreadPoolExecutor() as executor:
        executor.map(monitor_file_integrity, files_to_monitor)

if __name__ == "__main__":
    main()
