import requests

def getUser(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    response = requests.get(f"https://discord.com/api/v9/users/@me", headers=headers)

    try:
        return response.json()['username']
    except:
        return response.status_code

tokenfile = open("tokens.txt")
tokens = tokenfile.read().splitlines()
print("Found", len(tokens), "Tokens")

for i in tokens:
    api_request = getUser(token=i)
    if api_request == 401:
        print("bruh", i, "token is invalid")
        with open("invalid.txt", "a+") as file:
            file.write(i+"\n")
    elif api_request != 401:
        print("yippie", i, "token is valid")
        with open("valid.txt", "a+") as file:
            file.write(i+"\n")
