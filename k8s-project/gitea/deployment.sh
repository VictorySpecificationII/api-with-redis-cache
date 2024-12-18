microk8s helm3 repo add gitea https://dl.gitea.io/charts
microk8s helm3 repo update
microk8s helm3 install -f values-gitea.yaml gitea gitea/gitea --version 10.6.0
