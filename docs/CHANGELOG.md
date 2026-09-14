# Changelog

All notable changes to this project will be documented in this file.

## [V0.2.0]

### Added

- AWS account security and cost controls
- Temporary browser-based AWS CLI authentication
- Private Amazon ECR repository
- Linux/AMD64 container image build and push
- ECR basic vulnerability scanning
- ECS Fargate task definition and service
- ECS task execution IAM role
- CloudWatch container logging
- Container health checks
- Restricted direct task access using a security-group `/32` rule
- AWS endpoint and logging validation
- ECS task-replacement recovery test
- Manual AWS deployment and troubleshooting documentation
- AWS resource cleanup verification

## [V0.1.0] 

### Added
- FastAPI application foundation
- `/health` endpoint
- `/version` endpoint
- `/heartbeat` endpoint
- `/status` HTML status page
- `/api/status` endpoint
- In-memory heartbeat storage
- Online, delayed and offline status calculation
- Automated endpoint tests
- Multi-stage Dockerfile
- Docker Compose deployment
- Traefik routing