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