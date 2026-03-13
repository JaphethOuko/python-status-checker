# python-status-checker

# Automated Web Service Monitor

![Website Monitor CI](https://github.com/YOUR-GITHUB-USERNAME/python-status-checker/actions/workflows/main.yml/badge.svg)

## 📌 Overview

A lightweight DevOps utility designed to monitor the availability of critical web endpoints. This project demonstrates the implementation of a **Continuous Integration (CI)** pipeline using **GitHub Actions** to automate script execution and environment validation.

## 🚀 Key Features

- **Automated Monitoring:** Python-based health checks for multiple web services.
- **CI/CD Pipeline:** Fully automated workflow triggered on every `push` or `pull_request` to the main branch.
- **Infrastructure as Code (Light):** Defined execution environment using YAML-based workflow configurations on `ubuntu-latest` runners.
- **Dependency Management:** Clean separation of logic and requirements using `requirements.txt`.

## 🛠 Tech Stack

- **Language:** Python 3.10
- **Automation:** GitHub Actions (YAML)
- **Libraries:** Requests (HTTP Library)
- **OS:** Linux (Ubuntu)

## 📁 Repository Structure

- `.github/workflows/main.yml`: The CI/CD pipeline configuration.
- `checker.py`: Core logic for status verification.
- `requirements.txt`: Project dependencies.

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone git@github.com:JaphethOuko/python-status-checker.git
   ```
