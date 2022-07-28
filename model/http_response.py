import json

class HTTPResponse:
    def __init__(self, status_code: int, response_body: dict) -> None:
        self.statusCode = status_code
        self.headers = {}
        self.headers['Content-type'] = 'application/json'
        self.body = json.dumps(response_body)