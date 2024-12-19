# TODO

 - DONE -> Traefik: Acts as the edge reverse proxy and load balancer for microservices in a Kubernetes cluster.
 - DONE -> Redis: Caching layer for backend API responses to improve performance.
 - DONE -> Memcached: Used for session storage and lightweight ephemeral caching.
 - YOU ARE HERE -> Jenkins: Manages continuous integration and builds.
 - Rundeck: Automates task orchestration like DB backups or deployment cleanup tasks.
 - GitLab Runners: Run CI/CD jobs triggered by GitLab for quick feedback on code quality.
 - Spinnaker: Handles multi-stage deployments to production.

# Groundwork

Install microk8s by
 - sudo snap install microk8s --classic
 - sudo usermod -aG microk8s $USER
 - newgrp microk8s
 - microk8s enable helm3 registry metallb registry dns

Allow insecure registry by running 
 - sudo mkdir -p /etc/docker && echo '{ "insecure-registries": ["localhost:32000"] }' | sudo tee /etc/docker/daemon.json > /dev/null && sudo systemctl restart docker


# Setup

Add
 - api.local
 - httpbin.local
 - jenkins.local

To your /etc/hosts file

# Build

Build API by
 - ./api/src/ci.sh

# Deploy

Run Traefik by
 - ./traefik/deployment.sh

Run PostgreSQL by
 - ./postgresql/deployment.sh

Run Redis by
 - ./redis/deployment.sh

Run memcached by
 - ./memcached/deployment.sh

Run Gitea by (currently unused in favor of GitHub)
 - ./gitea.deployment.sh

Run Jenkins by
 - ./jenkins/deployment.sh

Run HTTPBin by
 - microk8s kubectl apply -f httpbin/httpbin.yaml

Run api by
 - microk8s kubectl apply -f api/api.yaml

# Specifics

Jumping from cafeteria to cafeteria with different network layouts? Inside the microk8s/ directory, there are instructions on how to add the
venue's subnet to metallb through a configmap. That should help you out.
