Exercise 1.1

Log output app — generates a random string on startup, prints it with a
timestamp every 5s. Containerized and deployed to a local k3d cluster.

Exercise 1.2

Todo app — Flask web server, prints startup message, port configurable via PORT env var. Deployed to k3d.

Exercise 1.3

Moved log-output deployment into a manifests/ folder (declarative convention). Verified with rollout restart and live log following.

Exercise 1.4

Created manifests/ folder for the todo app deployment (declarative convention). Verified with rollout restart and log following.

Exercise 1.5

Added a GET route to the todo app returning an HTML page. Confirmed access from the browser via kubectl port-forward.

Exercise 1.6

Added a NodePort Service to expose the todo app. Accessible at localhost:8082 via the k3d port mapping (no port-forward needed).

Exercise 1.7

Rewrote log-output as a Flask web server: background thread keeps the 5s logging, added a / endpoint returning timestamp + random string. Exposed via ClusterIP Service + Ingress (localhost:8081).