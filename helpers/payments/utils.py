import time
from .mpesa_utils import *

base_url = "https://lions-sight-first.herokuapp.com"


def mpesa_paybill(PhoneNumber, Amount):
    formatted_time = get_timestamp()
    decoded_password = generate_password(formatted_time)
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token}

    # getting phone number and Amount
    BusinesShortCode = "174379"

    request = {
        "BusinessShortCode": BusinesShortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": Amount,
        "PartyA": PhoneNumber,
        "PartyB": "174379",
        "PhoneNumber": PhoneNumber,
        "CallBackURL": base_url + "/mpesa_callback",
        "AccountReference": "test aware",
        "TransactionDesc": "Lions Test App",
    }

    if PhoneNumber != "" and Amount != "":
        response = requests.post(api_url, json=request, headers=headers)
        resp = response.json()
        if "errorCode" in resp:
            result = {
                'code': 1,
                'ResultDesc': 'Something went wrong'
            }
            return result
        else:
            print("jump")
            if resp['ResponseCode'] == "0":
                result = mpesa_confirmation(
                    headers,
                    PhoneNumber,
                    BusinesShortCode,
                    decoded_password,
                    formatted_time,
                    resp['CheckoutRequestID']
                )
                return result

            else:
                result = {
                    'code': 1,
                    'ResultDesc': 'Something went wrong'
                }
                return result


def mpesa_confirmation(Headers, PhoneNumber, BusinesShortCode, decoded_password, formatted_time, CheckoutRequestID):
    query_url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"

    request_query = {
        "BusinessShortCode": BusinesShortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "CheckoutRequestID": CheckoutRequestID
    }

    response = requests.post(query_url, json=request_query, headers=Headers)
    final_response = response.json()
    transaction_processed = mpesa_transaction_processed(final_response)

    while transaction_processed == True:
        time.sleep(3)
        response = requests.post(query_url, json=request_query, headers=Headers)
        final_response = response.json()
        transaction_processed = mpesa_transaction_processed(final_response)
    else:
        if str(final_response['ResultCode']) in str(0):
            # print(working)
            result = {
                'code': 0,
                'ResultDesc': final_response['ResultDesc'],
                'ResultCode': final_response['ResultCode']
            }
            return result
        else:
            result = {
                'code': 1,
                'ResultDesc': final_response['ResultDesc'],
                'ResultCode': final_response['ResultCode']
            }
            return result


# Insufficient funds
# {'code': 1, 'ResultDesc': 'The balance is insufficient for the transaction', 'ResultCode': '1'}

# Transaction being processed {'requestId': 'ws_CO_210920201326545383', 'errorCode': '500.001.1001', 'errorMessage':
# 'The transaction is being processed'}

def mpesa_transaction_processed(result):
    try:
        if result['errorCode'] == '500.001.1001':
            return True

    except KeyError:
        return False