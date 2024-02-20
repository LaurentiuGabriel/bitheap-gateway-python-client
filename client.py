import requests

class BitHeapGatewayClient:
    BASE_URL = 'https://bitheap-gateway.com'

    @staticmethod
    def request_payment(expect, currency, message, seller, customer, callback_url, account_id):
        url = f"{BitHeapGatewayClient.BASE_URL}/request_payment/{expect}/{currency}/{message}/{seller}/{customer}/{callback_url}/{account_id}"
        return requests.get(url)

    @staticmethod
    def check_payment(address):
        url = f"{BitHeapGatewayClient.BASE_URL}/check_payment/{address}"
        return requests.get(url)

    @staticmethod
    def payout(seller, amount, currency, address, account_id):
        url = f"{BitHeapGatewayClient.BASE_URL}/payout/{seller}/{amount}/{currency}/{address}/{account_id}"
        return requests.get(url)

    @staticmethod
    def get_seller_balance(seller):
        url = f"{BitHeapGatewayClient.BASE_URL}/get_seller_balance/{seller}"
        return requests.get(url)
