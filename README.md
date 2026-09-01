# Homelab Sentinel

> Monitoring hosted inside my homelab cannot report a complete homelab, power or internet failure. Homelab Sentinel will run independently in AWS, receive outbound heartbeats from the homelab and notify me when those heartbeats stop.

&nbsp;

# 🛣️ Roadmap

| Version  | Focus | Status |
|----------|-------|--------|
| V0.1.0   | Local Sentinel application | ✅ Completed |
| V0.2.0   | Manual AWS learning spike | 🚧 In Progress |
| V0.3.0   | Terraform deployment | ⏳ Planned |
| V0.4.0   | GitHub Actions CI/CD | ⏳ Planned |
| V0.5.0   | Homelab integration and alerting | ⏳ Planned |
| V1.0.0   | Tested portfolio release | ⏳ Planned |

&nbsp;

# Success Criteria

- Receive an authenticated HTTPS heartbeat from the homelab.
- Persist when the homelab was last seen.
- Report online, delayed or offline.
- Send an email after the missed-heartbeat threshold.
- Provision and destroy AWS infrastructure with Terraform.
- Deploy through GitHub Actions using AWS OIDC.
- Provide logs through CloudWatch.
- Document costs, security decisions and architectural trade-offs.

&nbsp;

## License

This project is licensed under the [MIT License](LICENSE).