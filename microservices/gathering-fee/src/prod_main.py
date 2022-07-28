# from service.service_output import ServiceOutput
from service.service_input import ServiceInput
from service.service import app
# from http_response import HTTPResponse
from request_body import RequestBody
import importlib.util
import sys
spec = importlib.util.spec_from_file_location("http_response", "/lib/model/http_response.py")
http_response = importlib.util.module_from_spec(spec)
sys.modules["http_response"] = http_response
spec.loader.exec_module(http_response)
# http_response.HTTPResponse()

def lambda_handler(event, context):
    try:
        request_body: dict = RequestBody(event).body
        service_input: ServiceInput = ServiceInput(request_body)
        service_output = app(service_input)
        return http_response.HTTPResponse(200, service_output.value).__dict__
    except TypeError as error:
        return http_response.HTTPResponse(500, {"Error message": str(error)}).__dict__
    

