import requests
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth

business_shortCode = "174379"
lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"


# getAccessToken
def generate_access_token():
    consumer_key = "wTyyD6i66KAnV7rQGzg7nkWPcgySzNeG"
    consumer_secret = "qehBFrdh8DEHIvXx"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    try:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    except:
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret), verify=False)

    json_response = (
        r.json()
    )

    my_access_token = json_response["access_token"]

    return my_access_token


# generate timestamp
def get_timestamp():
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

    return formatted_time


# generate passsword
def generate_password(formatted_time):
    data_to_encode = (
            business_shortCode + lipa_na_mpesa_passkey + formatted_time
    )

    encoded_string = base64.b64encode(data_to_encode.encode())
    # print(encoded_string) b'MjAxOTAyMjQxOTUwNTc='
    decoded_password = encoded_string.decode("utf-8")

    return decoded_password
