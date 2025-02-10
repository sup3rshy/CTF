#!/usr/bin/python3 
import dis 
import random
import os

def generate_password(i):
    password = random.getrandbits(32) * (i ^ 195894762 ^ 322420958) * 2969596945
    return password

def main():
    seed = int.from_bytes(os.urandom(8), "big")
    random.seed(seed)

    flag = "W1{this_is_a_fake_flag}"

    print("Vault is locked! Enter the password to unlock.")

    i = 1
    while True:
        password = generate_password(i)
        attempt = input("> ")
        
        if not attempt.isdigit():
            print("Invalid input! Enter a number.")
            continue
        
        difference = abs(password - int(attempt))
        
        if difference == 0:
            print("Access Granted! Here is your flag:", flag)
            break
        else:
            print(f"Access Denied! You are {difference} away from the correct password. Try again!")
        
        i = i + 1
    return None
    
main()