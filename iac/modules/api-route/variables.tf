variable "api_id" {
  type = string
}

variable "resource_name" {
  type = string
}

variable "ms_name" {
  type = string
}

variable "http_method" {
  type = string
}

variable "lambda_function_invoke_arn" {
  description = "Lambda's Arn for API Gateway to invoke lambda"
}