import requests

# Set the authorization token


def get_data(_url):
    printify_api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6ImM0ZGVlNThhZTFhNTBkYzA5ZDBkNDFiZmRiNGExODgwOTQ4M2E0YzUxZWJjZDY4OThlOTMwYWM4NDY2ZGMwNTZjOTA1Y2YyZGUyY2NhMDE1IiwiaWF0IjoxNzAyMzc3NjIxLjg0OTM1NiwibmJmIjoxNzAyMzc3NjIxLjg0OTM1OSwiZXhwIjoxNzM0MDAwMDIxLjg0MDA4OCwic3ViIjoiMTYyNjEzNTYiLCJzY29wZXMiOlsic2hvcHMubWFuYWdlIiwic2hvcHMucmVhZCIsImNhdGFsb2cucmVhZCIsIm9yZGVycy5yZWFkIiwib3JkZXJzLndyaXRlIiwicHJvZHVjdHMucmVhZCIsInByb2R1Y3RzLndyaXRlIiwid2ViaG9va3MucmVhZCIsIndlYmhvb2tzLndyaXRlIiwidXBsb2Fkcy5yZWFkIiwidXBsb2Fkcy53cml0ZSIsInByaW50X3Byb3ZpZGVycy5yZWFkIl19.ADuIC6EtBY8ceAWCFkNZBTBZY_LGTKc9F-SLtlBycAuhFB-trdxZhZOqlYrd9ekjSZZLgx6mBA4mqvwKt1s"
    # Set the request headers
    headers = {
        "Authorization": f"Bearer {printify_api_token}",
        "User-Agent": "Python Client"
    }

    # Set the API endpoint URL
    base_url = 'https://api.printify.com'
    url = base_url + _url
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        return data
        # print(data)
        # Process the response data as needed
        # ...
    else:
        print("Request failed with status code:", response.status_code)
        return None

def post_data(_url, json_data):
    printify_api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6ImM0ZGVlNThhZTFhNTBkYzA5ZDBkNDFiZmRiNGExODgwOTQ4M2E0YzUxZWJjZDY4OThlOTMwYWM4NDY2ZGMwNTZjOTA1Y2YyZGUyY2NhMDE1IiwiaWF0IjoxNzAyMzc3NjIxLjg0OTM1NiwibmJmIjoxNzAyMzc3NjIxLjg0OTM1OSwiZXhwIjoxNzM0MDAwMDIxLjg0MDA4OCwic3ViIjoiMTYyNjEzNTYiLCJzY29wZXMiOlsic2hvcHMubWFuYWdlIiwic2hvcHMucmVhZCIsImNhdGFsb2cucmVhZCIsIm9yZGVycy5yZWFkIiwib3JkZXJzLndyaXRlIiwicHJvZHVjdHMucmVhZCIsInByb2R1Y3RzLndyaXRlIiwid2ViaG9va3MucmVhZCIsIndlYmhvb2tzLndyaXRlIiwidXBsb2Fkcy5yZWFkIiwidXBsb2Fkcy53cml0ZSIsInByaW50X3Byb3ZpZGVycy5yZWFkIl19.ADuIC6EtBY8ceAWCFkNZBTBZY_LGTKc9F-SLtlBycAuhFB-trdxZhZOqlYrd9ekjSZZLgx6mBA4mqvwKt1s"
    # Set the request headers
    headers = {
        "Authorization": f"Bearer {printify_api_token}",
        "User-Agent": "Python Client"
    }

    # Set the API endpoint URL
    base_url = 'https://api.printify.com'
    url = base_url + _url
    if json_data is None:
        response = requests.post(url, headers=headers)
    else:
        response = requests.post(url, headers=headers, json=json_data)

    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        return data
        # print(data)
        # Process the response data as needed
        # ...
    else:
        print("Request failed with status code:", response.status_code)
        return None

# shop_url = '/v1/shops.json'
# data = get_data(shop_url)
# shop_id = data[0]['id']
shop_id = 13210475

# buleprint_url = '/v1/catalog/blueprints.json'
# data = get_data(buleprint_url)
# for i in range(len(data)):
#     if data[i]['title'] == 'Unisex Classic Tee':
#         print(i)
#         print(data[i])
#         blueprint_id = data[i]['id']
blueprint_id = 725
# provider_url = f'/v1/catalog/blueprints/{blueprint_id}/print_providers.json'
# provider_data = get_data(provider_url)
# print_provider_id = provider_data[0]['id']
# print_provider_id = provider_data[2]['id'] # 61
# Out[46]: 
# [{'id': 270, 'title': 'Dimona Tee facility (Chicago, US)'},
#  {'id': 74, 'title': 'Ink Blot'},
#  {'id': 61, 'title': 'Dimona Tee'},
#  {'id': 155, 'title': 'Dimona Tee facility (Miami, US)'},
#  {'id': 54, 'title': 'JAMS Designs'},
#  {'id': 39, 'title': 'SwiftPOD'}]
print_provider_id = 61

# variants_url = f'/v1/catalog/blueprints/{blueprint_id}/print_providers/{print_provider_id}/variants.json'
# data = get_data(variants_url)
#   {'id': 73871,
#    'title': 'Black / S',
#    'options': {'color': 'Black', 'size': 'S'},
#    'placeholders': [{'position': 'back', 'height': 2761, 'width': 2419},
#     {'position': 'front', 'height': 2761, 'width': 2419}]},
#   {'id': 73873,
#    'title': 'Black / M',
#    'options': {'color': 'Black', 'size': 'M'},
#    'placeholders': [{'position': 'back', 'height': 3436, 'width': 3009},
#     {'position': 'front', 'height': 3436, 'width': 3009}]},
#   {'id': 73879,
#    'title': 'Black / 2XL',
#    'options': {'color': 'Black', 'size': '2XL'},
#    'placeholders': [{'position': 'back', 'height': 4110, 'width': 3600},
#     {'position': 'front', 'height': 4110, 'width': 3600}]},

url_post = f'/v1/shops/{shop_id}/products.json'


def create_product(title, description, blueprint_id, print_provider_id, variant_ids, img_id, variant_prices):
    # price is in cents, 3000 means 30.00 dollars
    json_data = {
        "title": title,
        "description": description,
        "blueprint_id": blueprint_id,
        "print_provider_id": print_provider_id,
        "variants": [
            {
                "id": variant_id,
                "price": variant_price,
                "is_enabled": True
            } for variant_id, variant_price in zip(variant_ids, variant_prices)
        ],
        "print_areas": [
            {
            "variant_ids": variant_ids,
            "placeholders": [
                {
                "position": "front",
                "images": [
                    {
                        "id": img_id, 
                        "x": 0.5, 
                        "y": 0.5, 
                        "scale": 1,
                        "angle": 0
                    }
                ]
                }
            ]
            }
        ]
    }
    url_post = f'/v1/shops/{shop_id}/products.json'
    data = post_data(url_post, json_data)
    product_id = data['id']
    return product_id

# product_id = '657998c480387a0641022225'

def publish_product(shop_id, product_id):
    product_url = f'/v1/shops/{shop_id}/products/{product_id}.json'
    data = get_data(product_url)
    img_url = data['images'][0]['src']

    publish_status_url = f'/v1/shops/{shop_id}/products/{product_id}/publishing_succeeded.json'
    json_data = {
        "external": {
            "id": product_id,
            "handle": img_url
        }
    }
    data = post_data(publish_status_url, json_data)

# file_path = 'https://lc-gluttony.s3.amazonaws.com/Db7SYRSourdq/G4kpOpUbLaElHd6QCd8pJ8zRFTVkz0v6/WechatIMG38.jpg'

# 73873
# address_to
# {
# "first_name": "John",
# "last_name": "Smith",
# "email": "example@msn.com",
# "phone": "0574 69 21 90",
# "country": "BE",
# "region": "",
# "address1": "ExampleBaan 121",
# "address2": "45",
# "city": "Retie",
# "zip": "2470"
# }

def post_order_new_product(external_id, print_provider_id, blueprint_id, variant_id, img_url, quantity, address_to):

    # create a new product and order it
    json_data = {
        "external_id": external_id, # used for our database, not printify
        "line_items": [
        {
            "print_provider_id": print_provider_id,
            "blueprint_id": blueprint_id,
            "variant_id": variant_id,
            "print_areas": {
            "front": img_url
            },
            "quantity": quantity
        }
        ],
        "shipping_method": 1,
        "is_printify_express": False,
        "send_shipping_notification": False,
        "address_to": address_to
    }

    post_url = f'/v1/shops/{shop_id}/orders.json'
    data = post_data(post_url, json_data)
    order_id = data['id']
    return order_id

def post_order(external_id, product_id, variant_id, quantity, address_to):

    # Order an existing product
    json_data ={
        "external_id": external_id, # used for our database, not printify
        "line_items": [
        {
            "product_id": product_id,
            "variant_id": variant_id,
            "quantity": quantity
        }
        ],
        "shipping_method": 1,
        "is_printify_express": False,
        "send_shipping_notification": False,
        "address_to": address_to
    }
    post_url = f'/v1/shops/{shop_id}/orders.json'
    data = post_data(post_url, json_data)
    order_id = data['id']
    return order_id


def cancel_order(order_id):
    cancel_url = f'/v1/shops/{shop_id}/orders/{order_id}/cancel.json'
    post_data(cancel_url, None)

def send_to_production(order_id):
    send_url = f'/v1/shops/{shop_id}/orders/{order_id}/send_to_production.json'
    post_data(send_url, None)
