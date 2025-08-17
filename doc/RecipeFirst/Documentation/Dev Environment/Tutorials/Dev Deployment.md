# Summary

Step by step instructions for deployment of the development environment with the newest patches

## Prerequisites

- Ensure RecipeFirst-Dev EC2 instance is running
- GitHub pull request has been merged

## Process

1. SSH into RecipeFirst-Dev

2. ssh -i ".ssh\RecipeFirst-DevAdmin.pem" ubuntu@ec2-16-52-42-204.ca-central-1.compute.amazonaws.com

3. Switch to recipefirst user, enter password
4. Navigate to /home/recipefirst/recipefirst

5. cd /home/recipefirst/recipefirst

6. Pull the latest changes

7. git pull