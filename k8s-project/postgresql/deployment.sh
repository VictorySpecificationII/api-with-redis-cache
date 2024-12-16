microk8s helm3 repo add bitnami https://charts.bitnami.com/bitnami
microk8s helm3 repo update
microk8s helm3 install -f values-postgresql.yaml postgresql bitnami/postgresql --version 16.3.1

#to upgrade the deployment
microk8s helm3 upgrade -f values-postgresql.yaml postgresql bitnami/postgresql --version 16.3.1
