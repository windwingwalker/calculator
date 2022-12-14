resource "aws_resourcegroups_group" "default" {
  name = var.project_name

  resource_query {
    query = <<JSON
{
  "ResourceTypeFilters": [
    "AWS::ApiGateway::RestApi",
    "AWS::ApiGateway::Stage",
    "AWS::CertificateManager::Certificate",
    "AWS::CloudFormation::Stack",
    "AWS::CloudFront::Distribution",
    "AWS::CloudFront::StreamingDistribution",
    "AWS::CloudTrail::Trail",
    "AWS::CloudWatch::Alarm",
    "AWS::Config::ConfigRule",
    "AWS::Cognito::IdentityPool",
    "AWS::Cognito::UserPool",
    "AWS::DynamoDB::Table",
    "AWS::EC2::Host",
    "AWS::EC2::Image",
    "AWS::EC2::Instance",
    "AWS::EC2::InternetGateway",
    "AWS::EC2::LaunchTemplate",
    "AWS::EC2::NatGateway",
    "AWS::EC2::RouteTable",
    "AWS::EC2::SecurityGroup",
    "AWS::EC2::Snapshot",
    "AWS::EC2::Subnet",
    "AWS::EC2::Volume",
    "AWS::EC2::VPC",
    "AWS::ECR::Repository",
    "AWS::EFS::FileSystem",
    "AWS::EKS::Cluster",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::ElasticLoadBalancingV2::TargetGroup",
    "AWS::Events::Rule",
    "AWS::Glacier::Vault",
    "AWS::IAM::InstanceProfile",
    "AWS::IAM::ManagedPolicy",
    "AWS::IAM::OpenIDConnectProvider",
    "AWS::IAM::SAMLProvider",
    "AWS::IAM::ServerCertificate",
    "AWS::IAM::VirtualMFADevice",
    "AWS::KMS::Key",
    "AWS::Lambda::Function",
    "AWS::Logs::LogGroup",
    "AWS::OpenSearchService::Domain",
    "AWS::Redshift::Cluster",
    "AWS::Redshift::ClusterParameterGroup",
    "AWS::Redshift::ClusterSecurityGroup",
    "AWS::Redshift::ClusterSubnetGroup",
    "AWS::Redshift::HSMClientCertificate",
    "AWS::RDS::DBCluster",
    "AWS::RDS::DBClusterParameterGroup",
    "AWS::RDS::DBClusterSnapshot",
    "AWS::RDS::DBInstance",
    "AWS::RDS::DBParameterGroup",
    "AWS::RDS::DBSecurityGroup",
    "AWS::RDS::DBSnapshot",
    "AWS::RDS::DBSubnetGroup",
    "AWS::RDS::EventSubscription",
    "AWS::RDS::OptionGroup",
    "AWS::RDS::ReservedDBInstance",
    "AWS::Route53::Domain",
    "AWS::Route53::HealthCheck",
    "AWS::Route53::HostedZone",    
    "AWS::Route53Resolver::ResolverEndpoint",
    "AWS::Route53Resolver::ResolverRule",
    "AWS::SES::ConfigurationSet",
    "AWS::SES::ContactList",
    "AWS::SES::DedicatedIpPool",
    "AWS::SES::Identity",
    "AWS::SNS::Topic",
    "AWS::SQS::Queue",
    "AWS::SSM::Document",
    "AWS::SSM::MaintenanceWindow",
    "AWS::SSM::ManagedInstance",
    "AWS::SSM::Parameter",
    "AWS::SSM::PatchBaseline",
    "AWS::SecretsManager::Secret",
    "AWS::S3::Bucket"
  ],
  "TagFilters": [
    {
      "Key": "Project",
      "Values": ["${var.project_name}"]
    }
  ]
}
JSON
  }
}