import hashlib

def crack_password(target_hash, dictionary_file):
    """
    Attempts to crack a SHA-256 hashed password using a dictionary file.
    """
    try:
        with open(dictionary_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                # Remove whitespace and get the word
                word = line.strip()
                
                # Hash the current word from the dictionary
                # (Most real-world systems store hashes, not plain text)
                guess_hash = hashlib.sha256(word.encode()).hexdigest()

                if guess_hash == target_hash:
                    return f"SUCCESS! Password found: {word}"
        
        return "Password not found in dictionary."
    
    except FileNotFoundError:
        return "Error: Dictionary file not found."

# --- Simulation ---
# Let's say the password is 'dragon123'
password_to_crack = "dragon123"
hashed_target = hashlib.sha256(password_to_crack.encode()).hexdigest()

print(f"Target Hash: {hashed_target}")
print("Starting dictionary attack...")

# Replace 'passwords.txt' with your actual wordlist path
result = crack_password(hashed_target, "passwords.txt")
print(result)