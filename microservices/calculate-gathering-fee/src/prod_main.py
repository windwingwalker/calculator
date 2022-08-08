# from service.service_output import ServiceOutput
from service.service_input import ServiceInput
from service.service import app
from request_body import RequestBody
import sys
sys.path.append('/lib/model')
from http_response import HTTPResponse

def lambda_handler(event, context):
    try:
        request_body: dict = RequestBody(event).body
        service_input: ServiceInput = ServiceInput(request_body)
        service_output = app(service_input)
        return HTTPResponse(200, service_output.value).__dict__
    except TypeError as error:
        return HTTPResponse(500, {"Error message": str(error)}).__dict__
    

