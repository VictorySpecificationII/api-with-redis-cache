microk8s helm3 repo add bitnami https://charts.bitnami.com/bitnami
microk8s helm3 repo update
microk8s helm3 install -f values-redis.yaml redis bitnami/redis