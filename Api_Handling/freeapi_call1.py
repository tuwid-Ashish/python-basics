import requests
"mongodb+srv://freeapi:Y1MbQRGBlO7Qq6Jb@clusterfa.zji7qge.mongodb.net"
def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    response_data = response.json()

    if response_data["success"] and "data" in response_data:
        user_data = response_data["data"]
        user_name = user_data["login"]["username"]
        user_location = user_data["location"]["country"]

        return f"My name is {user_name} living in {user_location}"
    else:
        raise Exception("failed to request for data ")
    

def main():
    try:
        print(fetch_random_user())
    except Exception as error:
        print(str(error))

if __name__ == "__main__":
    main()