import requests


class PrintifyClient:
    def __init__(self, client, access_token):
        self.client = client
        self.access_token = access_token

    def request(self, method, uri='', data={}):
        headers = {'Authorization': 'Bearer ' + self.access_token}
        options = {'headers': headers}

        if data:
            options['json'] = data

        response = self.client.request(method, uri, **options)
        
        return response.json()


class PrintifyImage:
    def __init__(self, client):
        self.client = client

    def upload_image(self, filename, url):
        data = self.client.request('POST', f'https://api.printify.com/v1/uploads/images.json', {'file_name': filename, 'url': url})
        img_id = data['id']
        return img_id

# example 
# printify_api_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzN2Q0YmQzMDM1ZmUxMWU5YTgwM2FiN2VlYjNjY2M5NyIsImp0aSI6ImM0ZGVlNThhZTFhNTBkYzA5ZDBkNDFiZmRiNGExODgwOTQ4M2E0YzUxZWJjZDY4OThlOTMwYWM4NDY2ZGMwNTZjOTA1Y2YyZGUyY2NhMDE1IiwiaWF0IjoxNzAyMzc3NjIxLjg0OTM1NiwibmJmIjoxNzAyMzc3NjIxLjg0OTM1OSwiZXhwIjoxNzM0MDAwMDIxLjg0MDA4OCwic3ViIjoiMTYyNjEzNTYiLCJzY29wZXMiOlsic2hvcHMubWFuYWdlIiwic2hvcHMucmVhZCIsImNhdGFsb2cucmVhZCIsIm9yZGVycy5yZWFkIiwib3JkZXJzLndyaXRlIiwicHJvZHVjdHMucmVhZCIsInByb2R1Y3RzLndyaXRlIiwid2ViaG9va3MucmVhZCIsIndlYmhvb2tzLndyaXRlIiwidXBsb2Fkcy5yZWFkIiwidXBsb2Fkcy53cml0ZSIsInByaW50X3Byb3ZpZGVycy5yZWFkIl19.ADuIC6EtBY8ceAWCFkNZBTBZY_LGTKc9F-SLtlBycAuhFB-trdxZhZOqlYrd9ekjSZZLgx6mBA4mqvwKt1s"
# client = PrintifyClient(requests.Session(), printify_api_token)

# file_path = 'https://lc-gluttony.s3.amazonaws.com/Db7SYRSourdq/G4kpOpUbLaElHd6QCd8pJ8zRFTVkz0v6/WechatIMG38.jpg'
# data_id = PrintifyImage(client).upload_image('sam.jpg', file_path)

# # img_id = '65796e1a673461283aaaee7d'

