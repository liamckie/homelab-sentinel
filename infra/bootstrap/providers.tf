provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = var.project_name
      Environment = "shared"
      ManagedBy   = "terraform"
    }
  }
}

data "aws_caller_identity" "current" {}

locals {
  state_bucket_name = "${var.project_name}-terraform-state-${data.aws_caller_identity.current.account_id}-${var.aws_region}"
}