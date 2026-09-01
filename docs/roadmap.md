# Roadmap


&nbsp;

# V0.1.0 — Local Sentinel application ![Status](https://img.shields.io/badge/Status-🚧%20In%20Progress-black)

<b>Goal:</b> Build and validate the smallest local version of Homelab Sentinel before introducing AWS infrastructure.

## Core features
- Small FastAPI application
- GET /health application health endpoint
- POST /heartbeat heartbeat receiver
- GET /status human-readable HTML status page
- GET /api/status machine-readable JSON status endpoint
- In-memory storage of the latest heartbeat
- Online, delayed and offline status calculation
- Automated endpoint tests
- Multi-stage Dockerfile
- Local Docker deployment

## Completion criteria
- The application runs locally using Python.
- The application runs successfully as a Docker container.
- Sending a heartbeat updates the recorded timestamp.
- The status endpoints reflect the age of the latest heartbeat.
- All automated tests pass.
- Local setup and verification commands are documented.

## Known limitations
- The latest heartbeat is stored in memory and is lost when the application restarts.
- The heartbeat endpoint is not yet authenticated.
- No AWS services or email notifications are included in this version.

&nbsp;

# V0.2.0 — Manual AWS Learning Deployment

<b>Goal:</b> Deploy the container manually to AWS to understand how the core services interact before automating them.

### Core features
- Amazon ECR repository
- Manual image build and push
- Amazon ECS cluster
- ECS Fargate task definition and service
- CloudWatch application logs
- Temporary public task access
- Security group restricted for testing
- ECS task replacement test
- Complete removal of the manual deployment after validation

&nbsp;

# V0.3.0 — Terraform Deployment

<b>Goal:</b> Create a reproducible AWS environment using Infrastructure as Code.

### Core features
- Terraform remote state
- VPC, subnets and routing
- Application and load-balancer security groups
- Amazon ECR repository
- CloudWatch log group
- ECS task execution and application roles
- ECS cluster, task definition and service
- Application Load Balancer
- ACM certificate
- Cloudflare DNS
- Reproducible terraform apply and terraform destroy workflow
- Documented cost and security decisions

&nbsp;

# V0.4.0 — Continuous Integration and Delivery

<b>Goal:</b> Automatically test, build and deploy application changes safely.

### Core features
- Python linting and automated tests
- Docker image build
- Container vulnerability scanning
- Immutable Git commit image tags
- Image publishing to Amazon ECR
- GitHub Actions authentication through AWS OIDC
- ECS task-definition update
- Deployment health verification
- Documented rollback procedure

&nbsp;

# V0.5.0 — Operational Sentinel Capability

<b>Goal:</b> Connect AWS to the homelab and provide independent outage detection.

### Core features
- DynamoDB heartbeat persistence
- Authenticated heartbeat ingestion
- Independent homelab heartbeat sender
- Configurable online, delayed and offline thresholds
- EventBridge scheduled status evaluation
- Lambda missed-heartbeat evaluator
- SNS outage and recovery notifications
- Simulated homelab outage
- Recovery and alert verification

&nbsp;

# V1.0.0 — Portfolio Release

<b>Goal:</b> Produce a tested, documented and reproducible release suitable for continued personal use and portfolio demonstration.

### Core deliverables
- Final architecture diagram
- Threat model and security decisions
- AWS cost breakdown
- Operational runbook
- Deployment and rollback evidence
- Outage and recovery test evidence
- Terraform recreation test
- Documented architectural trade-offs
- Known limitations and future improvements
- Polished project README