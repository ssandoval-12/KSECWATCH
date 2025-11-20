from flask import Flask, Response
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Métricas de seguridad
LOGIN_FAILURES = Counter('security_login_failures_total', 'Number of failed logins')
UNAUTHORIZED   = Counter('security_unauthorized_attempts_total', 'Unauthorized access attempts')
CONFIG_CHANGES = Counter('security_config_changes_total', 'Configuration changes detected')

@app.route('/login-fail')
def login_fail():
    LOGIN_FAILURES.inc()
    return "Login failed recorded."

@app.route('/unauthorized')
def unauthorized():
    UNAUTHORIZED.inc()
    return "Unauthorized access recorded."

@app.route('/config-change')
def config_change():
    CONFIG_CHANGES.inc()
    return "Config change recorded."

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
