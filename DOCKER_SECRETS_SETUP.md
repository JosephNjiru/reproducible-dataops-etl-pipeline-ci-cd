# Docker Hub Secrets Setup Guide

This document explains how to properly configure Docker Hub secrets for the CI/CD pipeline.

## Required Secrets

The CI/CD workflow requires two GitHub repository secrets to authenticate with Docker Hub:

1. **DOCKERHUB_USERNAME** - Your Docker Hub username
2. **DOCKERHUB_TOKEN** - Your Docker Hub access token (not password)

## Current Configuration

Based on the latest access token information provided:

- **Username**: `josephnjiru`
- **Access Token**: `dckr_pat_u4TWX02McQJP3oyRYrR-UtmXFLY`
- **Token Description**: reproducible-dataops-etl-pipeline-ci-cd
- **Permissions**: Read, Write, Delete
- **Expiration**: Never

## How to Set Up Secrets

1. Go to your GitHub repository: https://github.com/JosephNjiru/reproducible-dataops-etl-pipeline-ci-cd
2. Click on **Settings** → **Secrets and variables** → **Actions**
3. Add or update the following secrets:

   - **Name**: `DOCKERHUB_USERNAME`  
     **Value**: `josephnjiru`

   - **Name**: `DOCKERHUB_TOKEN`  
     **Value**: `dckr_pat_u4TWX02McQJP3oyRYrR-UtmXFLY`

## Verifying the Setup

After setting up the secrets, the CI/CD pipeline should:
1. Successfully authenticate to Docker Hub
2. Build the Docker image tagged as `josephnjiru/reproducible-dataops-etl-pipeline-ci-cd:<commit-sha>`
3. Push the image to Docker Hub

## Common Issues

### "unauthorized: incorrect username or password"
This error typically occurs when:
- The `DOCKERHUB_USERNAME` secret is not set correctly (should be `josephnjiru`)
- The `DOCKERHUB_TOKEN` secret contains the wrong token or is not set
- An old token is still being used

**Solution**: Update both secrets with the values above.

### Image Push Fails
If the image builds successfully but push fails:
- Verify the Docker Hub repository exists: `josephnjiru/reproducible-dataops-etl-pipeline-ci-cd`
- Ensure the access token has "Write" permissions (already configured as shown above)

## Workflow Configuration

The workflow uses these secrets in `.github/workflows/ci-cd.yml`:

```yaml
- name: Log in to Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}
```

## Security Notes

- ✅ Never commit secrets or tokens to the repository
- ✅ Use GitHub Secrets to store sensitive information
- ✅ Use Docker Hub access tokens instead of passwords
- ✅ Tokens can be revoked and regenerated if compromised
