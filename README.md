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

Exercise 1.8

Switched the todo app from NodePort to ClusterIP + Ingress (localhost:8081). Removed the log-output Ingress from the cluster to avoid path collision.

Exercise 1.9

Built the ping-pong app: /pingpong returns "pong N" with an in-memory counter that increments per request. Shares one Ingress with log-output — / routes to log-output, /pingpong routes to ping-pong.

Exercise 1.10

Split log-output into two containers in one pod: a writer (generates the random string, writes timestamp + string to a file every 5s) and a reader (serves the file's contents over HTTP). They share data via an emptyDir volume mounted at /usr/src/app/files in both containers.

Exercise 1.11

Shared a PersistentVolume between ping-pong and log-output (separate pods). ping-pong writes its counter to a file on the PVC; log-output's reader reads it and shows "Ping / Pongs: N" alongside the timestamp and random string. PV/PVC definitions kept in a separate top-level manifests/ folder.