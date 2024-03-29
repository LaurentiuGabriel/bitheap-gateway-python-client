# BitHeap Gateway Python Client

The `bitheap_gateway_client` is a Python package designed for e-commerce and retail platforms to facilitate Bitcoin payments. It simplifies the process of integrating Bitcoin payment functionality, including generating QR codes for Bitcoin transactions.

## Features

- Request Bitcoin payments with QR code generation.
- Check the status of Bitcoin payments.
- Execute payouts in Bitcoin.
- Retrieve a seller's Bitcoin balance.

## Installation

To install `bitheap_gateway_client`, simply use pip:

```bash
pip install bitheap_gateway_client
```

## Usage
Here's how to use the bitheap_gateway_client in your Python project:

### Importing the Client

```python
from bitheap_gateway_client.client import BitHeapGatewayClient
```

### Requesting a Payment


```python
response = BitHeapGatewayClient.request_payment('expect', 'currency', 'message', 'seller', 'customer', 'callback_url', 'account_id')
print(response.json())
```

### Checking Payment Status

```python
response = BitHeapGatewayClient.check_payment('address')
print(response.json())
```

### Processing a Payout

```python
response = BitHeapGatewayClient.payout('seller', 'amount', 'currency', 'address', 'account_id')
print(response.json())
```

### Getting Seller's Balance

```python
response = BitHeapGatewayClient.get_seller_balance('seller')
print(response.json())
```

## Contributions
Contributions are welcome! Please feel free to submit pull requests or open issues to improve the functionality or efficiency of this package.

## License
This project is licensed under the MIT License - see the LICENSE file for details.