pipeline{
  agent any
  environment {
    AWS_ACCESS_KEY_ID          = credentials('aws_access_key_id')
    AWS_SECRET_ACCESS_KEY      = credentials('aws_secret_access_key')
    AWS_ACCOUNT_ID             = credentials('aws_account_id')
    
    PROJECT_NAME               = "calculator"

    TF_VAR_project_name        = "${PROJECT_NAME}"
    TF_VAR_aws_account_id      = "${AWS_ACCOUNT_ID}"    
  }
  tools {
    terraform 'TerraformDefault'
  }
  options {
    ansiColor('xterm')
  }
  stages{
    stage('Deploy'){
      steps{
        dir('iac'){
          sh 'terraform init -input=false'
          sh 'terraform plan -out=tfplan -input=false'
          sh 'terraform apply -input=false -auto-approve tfplan'
        }
      }
    }
  }
}