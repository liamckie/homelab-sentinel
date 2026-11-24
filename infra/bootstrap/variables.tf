variable "aws_region" {
  description = "AWS region containing the Terraform state bucket"
  type        = string
  default     = "eu-west-2"
}

variable "project_name" {
  description = "Project name used when naming and tagging resources"
  type        = string
  default     = "homelab-sentinel"
}