# Contributing to KSECWATCH

Thank you for considering contributing to the **KSECWATCH** project!  
We welcome contributions such as bug fixes, improvements, new alerts, dashboards, or documentation updates.

This project is designed for SRE/Monitoring education, using Kubernetes, Prometheus Operator, Alertmanager and Python/Flask.

---

## 🚀 How to Contribute

### 1. **Fork the Repository**

Click the **Fork** button at:  
https://github.com/ssandoval-12/KSECWATCH


### 2. **Clone Your Fork**

git clone https://github.com/your-username/KSECWATCH.git
cd KSECWATCH


### 3. **Create a New Branch**

git checkout -b feature/your-feature-name


### 4. Make Your Changes

Examples of changes you may contribute:

New Prometheus metrics
-New alerting rules
-Dashboard improvements
-Kubernetes manifest enhancements
README or documentation updates

Before committing:
-Validate Kubernetes YAML files:
kubectl apply --dry-run=client -f file.yaml

-Validate Prometheus rules:
promtool check rules <file>

### 5. Commit and Push

git add .
git commit -m "Describe your change here"
git push origin feature/your-feature-name

### 6. Open a Pull Request

-Go to your fork on GitHub
-Click “Compare & pull request”
-Add a clear description of your change and why it’s useful

### 🧭 Code Style & Guidelines

-Use descriptive variable and alert names
-Follow Kubernetes YAML indentation (2 spaces)
-Keep Prometheus rules clear and simple
-Update documentation when adding new features
-Never include secrets (Slack webhook, passwords, tokens, etc.)

### 💬 Communication

For major ideas or changes, consider opening an Issue first.
Be respectful, constructive and collaborative.

### Thank you for helping improve KSECWATCH!