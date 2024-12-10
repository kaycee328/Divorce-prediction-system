import requests


def get_linkedin_user_info(access_token):
    url = "https://api.linkedin.com/v2/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json()


token = ""
get_linkedin_user_info(token)
