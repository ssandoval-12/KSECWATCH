# 🚀 KSECWATCH – Security & Pod Monitoring for Kubernetes  
Full Observability Stack: Minikube + Prometheus Operator + Grafana + Alertmanager + Slack

KSECWATCH is a security-focused monitoring application built with **Python/Flask**, exposing custom Prometheus metrics and deployed on Kubernetes.  
The project includes a complete observability pipeline with:

- Prometheus (metrics scraping)
- Alertmanager (Slack alerts with emojis)
- Grafana (dashboards)
- Custom PrometheusRules (security & pod alerts)
- ServiceMonitor (Prometheus Operator)
- Secure Slack secret (not stored in repo)
- Minikube deployment

---

# 📂 Repository Structure
```text
.
├── application
│ ├── main.py
│ └── requirements.txt
│
├── kubernetes
│ ├── deployment.yaml
│ ├── service.yaml
│ ├── ksecwatch-servicemonitor.yaml
│ ├── security-alerts.yaml
│ ├── pod-changes-alerts.yaml
│ └── alertmanagerconfig-ksecwatch.yaml
│
├── dashboards
│ └── security-pod-dashboard.json
│
├── screenshots
│ ├── slack.png
│ ├── alertmanager.png
│ ├── grafana.png
│ └── prometheus.png
│
├── .gitignore
└── README.md
```
---

# ⚙️ Requirements

- Minikube (Docker driver)
- Docker
- Helm 3
- kubectl
- Python 3.9+
- Slack Webhook URL

---

# 🧹 1. Wipe Environment (Clean Start)

minikube delete --all --purge <br>
docker system prune -af --volumes <br>
rm -rf ~/.kube ~/.minikube

---

# 🚀 2. Start Minikube

minikube start --driver=docker --memory=4096 --cpus=2
kubectl create namespace monitoring

---

# 📦 3. Build & Load Docker Image

docker build -t ksecwatch-app:0.1 .
minikube image load ksecwatch-app:0.1

---

# 📥 4. Install kube-prometheus-stack (with Grafana password)

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install kps prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --set grafana.adminPassword="NuevaPass123!" \
  --set grafana.service.type=ClusterIP \
  --set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=false \
  --set prometheus.prometheusSpec.ruleSelectorNilUsesHelmValues=false

---

# 🔐 5. Create Secure Slack Secret

kubectl create secret generic slack-webhook \
  --from-literal=url="https://hooks.slack.com/services/XXX/YYY/ZZZ" \
  -n monitoring

---

# 🚀 6. Deploy KSECWATCH & Monitoring Rules

kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/ksecwatch-servicemonitor.yaml
kubectl apply -f kubernetes/security-alerts.yaml
kubectl apply -f kubernetes/pod-changes-alerts.yaml
kubectl apply -f kubernetes/alertmanagerconfig-ksecwatch.yaml

---

# 📡 7. Access UIs

Prometheus
kubectl port-forward svc/kps-kube-prometheus-stack-prometheus -n monitoring 9091:9090
http://localhost:9091

Alertmanager
kubectl port-forward svc/kps-kube-prometheus-stack-alertmanager -n monitoring 9003:9093
http://localhost:9003

Grafana
kubectl port-forward svc/kps-grafana -n monitoring 3001:80
http://localhost:3001
Login:
admin / NuevaPass123!

---

# 📊 8. Import Dashboard

Upload this file in Grafana:
dashboards/security-pod-dashboard.json

---

# 🧪 9. Testing

Trigger metrics
kubectl port-forward deploy/ksecwatch -n monitoring 8000:8000
curl localhost:8000/login-fail
curl localhost:8000/unauthorized
curl localhost:8000/config-change

Generate alert spike
for i in {1..15}; do curl localhost:8000/login-fail; done

---

# 🛎️ 10. Slack Notifications

FIRING Example:
🚨 [FIRING] LoginFailureSpike
🔥 Severity: warning
🧩 Project: ksecwatch
📂 Category: auth
📝 Description: High volume of failed logins detected.

RESOLVED Example:
🟢 [RESOLVED] LoginFailureSpike
👌 Issue has been resolved.

---

# 🖼️ 11. Screenshots

Slack Alerts
Alertmanager UI
Grafana Dashboard
Prometheus Targets

---

# 🛠️ 12. Troubleshooting

Pod not scraped
Check matchLabels in ServiceMonitor:
   selector:
  matchLabels:
    app: ksecwatch

Slack not receiving alerts
Verify secret exists:
kubectl get secret slack-webhook -n monitoring -o yaml

Dashboard shows no alerts
PromQL query must include:
ALERTS{alertstate="firing"}

---

# 13. 🎉 KSECWATCH Completed!


