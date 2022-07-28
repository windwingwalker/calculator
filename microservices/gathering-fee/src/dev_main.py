import json
from service.service import app
from service.service_input import ServiceInput
# from service.service_output import ServiceOutput

if __name__ == '__main__':
    f = open("../input.json")
    data = json.load(f)
    
    service_output = app(ServiceInput(data))
    
    print(service_output.__dict__)
    