provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "homelab-sentinel"
      Environment = "development"
      ManagedBy   = "terraform"
    }
  }
}