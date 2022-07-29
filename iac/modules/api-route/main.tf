data "aws_apigatewayv2_api" "default" {
  api_id = var.api_id
}

resource "aws_apigatewayv2_integration" "default" {
  api_id = var.api_id

  integration_uri    = "arn:aws:apigateway:${var.aws_region}:lambda:path/2015-03-31/functions/${var.function_arn}:$${stageVariables.alias}/invocations"
  integration_type   = "HTTP_PROXY"
  integration_method = "POST"
}

# resource "aws_apigatewayv2_route" "default" {
#   api_id = var.api_id

#   route_key = "${var.http_method} /${var.resource_name}"
#   target    = "integrations/${aws_apigatewayv2_integration.default.id}"

#   depends_on = [
#     aws_apigatewayv2_integration.default
#   ]
# }

resource "aws_lambda_permission" "default" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = var.ms_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${data.aws_apigatewayv2_api.default.execution_arn}/*/*"
}