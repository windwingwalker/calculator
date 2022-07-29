FROM public.ecr.aws/lambda/python:3.8

# Copy function code
WORKDIR ${LAMBDA_TASK_ROOT}
COPY model/ /lib/model/
COPY src/ .
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "prod_main.lambda_handler" ] 