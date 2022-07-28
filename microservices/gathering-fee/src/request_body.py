import json

class RequestBody:
    def __init__(self, event) -> None:   
        self.body = self.get_body_from_event(event)

    def get_body_from_event(self, event):
        body = json.dumps(str(event['body']).replace("\n", ""))
        body = json.loads(body)
        body = eval(body)
        return body
