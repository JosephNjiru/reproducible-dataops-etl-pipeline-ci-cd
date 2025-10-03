# Security Policy

## Dependency Security Status

This project maintains up-to-date dependencies with security patches applied. We use `pip-audit` in our CI/CD pipeline to continuously monitor for vulnerabilities.

### Current Security Posture

✅ **All fixable vulnerabilities have been resolved.**

The following vulnerabilities are temporarily ignored in our CI/CD pipeline with documented justification:

| Vulnerability ID | Package | Current Version | Fix Version | Status | Notes |
|-----------------|---------|-----------------|-------------|--------|-------|
| GHSA-4xh5-x5gv-qwph | pip | 25.2 | 25.3 | 🔶 Pending | Fix planned for pip 25.3 (not yet released). Will update immediately upon release. |
| PYSEC-2024-75 | twisted | 24.3.0 | 24.7.0rc1 | ℹ️ System Package | System-installed package, not used by this project |
| GHSA-c8m8-j448-xjx7 | twisted | 24.3.0 | 24.7.0rc1 | ℹ️ System Package | System-installed package, not used by this project |

### Recently Fixed Vulnerabilities (Latest Update)

- ✅ **requests**: Upgraded from 2.31.0 → 2.32.5 (Fixed 2 CVEs)
- ✅ **setuptools**: Upgraded from 68.1.2 → 80.9.0 (Fixed 1 CVE)
- ✅ **urllib3**: Upgraded from 2.0.7 → 2.5.0 (Fixed 1 CVE)
- ✅ **jinja2**: Upgraded from 3.1.2 → 3.1.6 (Fixed 5 CVEs)
- ✅ **certifi**: Upgraded from 2023.11.17 → 2025.8.3 (Fixed 1 CVE)
- ✅ **cryptography**: Upgraded from 41.0.7 → 46.0.2 (Fixed 4 CVEs)
- ✅ **idna**: Upgraded from 3.6 → 3.10 (Fixed 1 CVE)
- ✅ **configobj**: Upgraded from 5.0.8 → 5.0.9 (Fixed 1 CVE)

### Security Best Practices

1. **Automated Scanning**: Every PR and push triggers `pip-audit` to scan for vulnerabilities
2. **Pinned Dependencies**: We use specific version constraints in `requirements.txt`
3. **Regular Updates**: Dependencies are reviewed and updated regularly
4. **Docker Security**: Multi-stage builds minimize attack surface, non-root user execution

### Reporting Security Issues

If you discover a security vulnerability in this project, please email the maintainer or open a private security advisory on GitHub.

### Update Schedule

- **Critical vulnerabilities**: Patched within 24 hours
- **High severity**: Patched within 1 week
- **Medium/Low severity**: Patched in next release cycle

---

**Last Updated**: 2025-01-20  
**Next Review**: When pip 25.3 is released
