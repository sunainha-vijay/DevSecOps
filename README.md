

# Challenge 3 - DevSecOps Demo

[![CI Pipeline](https://github.com/sunainha-vijay/challenge3/actions/workflows/ci.yml/badge.svg)](https://github.com/sunainha-vijay/challenge3/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=sunainha-vijay_challenge3&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=sunainha-vijay_challenge3)
[![SonarQube Cloud](https://sonarcloud.io/images/project_badges/sonarcloud-dark.svg)](https://sonarcloud.io/summary/new_code?id=sunainha-vijay_challenge3)

This repository contains a simple Flask-based calculator API created to demonstrate a fundamental DevSecOps workflow. The project integrates automated security and quality checks directly into a Continuous Integration (CI) pipeline using GitHub Actions.


## Objective
The primary objective of this challenge is to showcase an understanding of DevSecOps principles by building an automated CI/CD pipeline. This pipeline serves as a "quality gate," ensuring that all code committed to the main branch is automatically tested, linted, and scanned for security vulnerabilities and code quality issues.

## Tech Stack
Language: Python 3.10

Framework: Flask

CI/CD: GitHub Actions

Code Linters: flake8

Security Scanning: Bandit

Testing: pytest

Advanced Code Analysis: SonarCloud



## Setup Steps
### Local Setup
To run this application on your local machine, follow these steps:

Clone the repository:

git clone https://github.com/sunainha-vijay/challenge3.git

cd challenge3


Create and activate a virtual environment:

python -m venv venv

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run the application:

python app.py


The API will be available at http://127.0.0.1:5000.


## Challenges & Assumptions Made
### 1. CI/CD Pathing and Import Errors
Challenge: The pytest and other scripts initially failed with ModuleNotFoundError and FileNotFoundError. This was due to the Python import path not being correctly configured within the GitHub Actions runner environment and an incorrect working-directory setting.

Assumption: A clean and standard project structure is essential for predictable CI builds.

Solution: The project structure was flattened to remove unnecessary nested directories. The CI workflow was then updated by removing the working-directory override, and the pytest command was run with PYTHONPATH=. to ensure modules within the project were discoverable from the test files.

### 2. SonarCloud Configuration
Challenge: The initial SonarCloud integration failed for two reasons:

Missing sonar.projectKey and sonar.organization properties.

A conflict between the CI-based analysis and SonarCloud's default "Automatic Analysis" feature.

Assumption: A CI-based analysis (using GitHub Actions) offers more control and is preferable for a DevSecOps pipeline over automatic analysis.

Solution:

A sonar-project.properties file was created in the repository's root to provide the scanner with the necessary project identity keys.

"Automatic Analysis" was disabled in the SonarCloud project settings, resolving the conflict.

### 3. Bandit Security Linter Warning
Challenge: The Bandit SAST tool flagged a medium-severity vulnerability (B104:hardcoded_bind_all_interfaces) on the line app.run(host="0.0.0.0"). This presented a conflict: this configuration is often necessary for containerized deployment environments (like Render) but is a security risk for local development on an open network.

Assumption/Principle: Security analysis must be context-aware. A configuration that is appropriate for a sandboxed production environment may be insecure for an uncontrolled local development environment.

Solution: The solution acknowledges that the if __name__ == "__main__": block is strictly for local development, as the Render deployment uses a production-grade WSGI server (Gunicorn) defined in its Start Command. Therefore, the code was modified to use the more secure host="127.0.0.1" for local execution. This satisfies the security linter for the relevant context (local development) without impacting the production deployment configuration.
