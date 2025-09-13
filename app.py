from flask import Flask
import bugsnag
from bugsnag.flask import handle_exceptions
from datadog import initialize, statsd

# -----------------------------
# Datadog Setup
# -----------------------------
# Replace <your_api_key> and <your_app_key> with actual values if using custom metrics.
# If you're only using the Datadog Agent (via Docker or Kubernetes), you don't need keys here.
options = {
    "api_key": "8e542605860ab495deadde28dfef6f5c",   # optional if using Datadog Agent
}
initialize(**options)

# -----------------------------
# Bugsnag Setup
# -----------------------------
bugsnag.configure(
    api_key="db4da5bc52009b3eeb7ae0084ff9f639",
    project_root="/path/to/your/app"
)

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)
handle_exceptions(app)  # attaches Bugsnag error handler to Flask


@app.route("/")
def home():
    # Send a custom metric to Datadog every time this endpoint is hit
    statsd.increment("flask_app.homepage.hit")
    return "Hello, DevOps Assessment with Datadog and Bugsnag for monitoring tool!!!"


@app.route("/error")
def error():
    # This will raise an exception and Bugsnag will capture it
    raise RuntimeError("Intentional error for Bugsnag demo!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

