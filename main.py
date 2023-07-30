import requests

def get_player_bans_data(api_key, steam_id):
    base_url = "https://api.steampowered.com/ISteamUser/GetPlayerBans/v1/"
    params = {
        "key": "A0E64641F9DBA02FBDBC399D96A6C1C1",
        "steamids": steam_id
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def main():
    api_key = "A0E64641F9DBA02FBDBC399D96A6C1C1"  # Replace this with your own Steam API key
    steam_id = input("Enter the Steam ID: ")

    data = get_player_bans_data(api_key, steam_id)

    if data:
        print("Player Bans Data:")
        print(data)
        # Process the data as needed
    else:
        print("Data retrieval failed.")

if __name__ == "__main__":
    main()
