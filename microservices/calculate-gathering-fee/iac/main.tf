terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.48.0"
    }
  }
 
  required_version = "~> 1.0"
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      "Project" = var.project_name
    }
  }
}

module "lambda" {
  source = "../../../iac/modules/lambda/"
  ms_name = var.ms_name
  image_tag = var.image_tag
}

module "api-route" {
  source = "../../../iac/modules/api-route/"
  api_id = var.api_id
  resource_name = var.resource_name
  ms_name = var.ms_name
  http_method = var.http_method
  lambda_function_invoke_arn = module.lambda.function_invoke_arn
}
