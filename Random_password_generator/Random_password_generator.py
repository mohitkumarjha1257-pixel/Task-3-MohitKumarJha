import string
import secrets
import math

def calculate_entropy(length, pool_size):
    """Calculates the mathematical entropy of the password."""
    # E = L * log2(R)
    entropy = length * math.log2(pool_size)
    return round(entropy, 2)    

def generate_password(length):
  
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    all_characters = letters + digits + symbols
    
    password_list = []
    
    length_pass = length
   
    for i in range(length_pass):
        random_char = secrets.choice(all_characters)
        password_list.append(random_char)
        
    secrets.SystemRandom().shuffle(password_list)
    
    final_password = "".join(password_list)

    pool_size = len(all_characters)
    
    entropy_score = calculate_entropy(length, pool_size)
    
    return final_password, entropy_score


try:
    print("--- Enterprise Random Password Generator ---")
    user_input = int(input("Enter desired password length (Min 15 recommended per NIST 2024): "))
    
    password, entropy = generate_password(user_input)
    
    print("\n[+] SUCCESS: Credentials Generated")
    print("Password: ", password)
    print("Entropy Score: ",entropy," bits")
    
except ValueError as e:
    print(f"\n[!] Input Error: {e}")