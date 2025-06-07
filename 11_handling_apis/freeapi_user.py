import requests # type: ignore

def fetch_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        
        all_user = {}
        for user in user_data["data"]:
            all_user[user["login"]["username"]] = user["location"]["country"]
        return all_user          
    
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        all_user = fetch_user_freeapi()
        for username, country  in all_user.items():
            print(f"Username: {username} \nCountry: {country}")

    except Exception as e:
        print(str(e))
        
        
if __name__ == "__main__":
    main()