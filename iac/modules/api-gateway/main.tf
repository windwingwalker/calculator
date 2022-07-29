resource "aws_apigatewayv2_api" "default" {
  name          = "${var.project_name}-gateway"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_stage" "dev" {
  api_id = aws_apigatewayv2_api.default.id

  name        = "dev"
  auto_deploy = true
  stage_variables = {
    "env" = "dev"
  }

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.default.arn

    format = jsonencode({
      requestId               = "$context.requestId"
      sourceIp                = "$context.identity.sourceIp"
      requestTime             = "$context.requestTime"
      protocol                = "$context.protocol"
      httpMethod              = "$context.httpMethod"
      resourcePath            = "$context.resourcePath"
      routeKey                = "$context.routeKey"
      status                  = "$context.status"
      responseLength          = "$context.responseLength"
      integrationErrorMessage = "$context.integrationErrorMessage"
      }
    )
  }
}

resource "aws_apigatewayv2_stage" "prod" {
  api_id = aws_apigatewayv2_api.default.id

  name        = "prod"
  auto_deploy = false
  stage_variables = {
    "env" = "prod"
  }

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.default.arn

    format = jsonencode({
      requestId               = "$context.requestId"
      sourceIp                = "$context.identity.sourceIp"
      requestTime             = "$context.requestTime"
      protocol                = "$context.protocol"
      httpMethod              = "$context.httpMethod"
      resourcePath            = "$context.resourcePath"
      routeKey                = "$context.routeKey"
      status                  = "$context.status"
      responseLength          = "$context.responseLength"
      integrationErrorMessage = "$context.integrationErrorMessage"
      }
    )
  }
}

resource "aws_cloudwatch_log_group" "default" {
  name = "/aws/api_gw/${aws_apigatewayv2_api.default.name}"

  retention_in_days = 30
}
