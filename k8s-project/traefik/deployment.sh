microk8s helm3 repo add traefik https://traefik.github.io/charts
microk8s helm3 repo update
microk8s helm3 install -f values-traefik.yaml traefik traefik/traefik
#to upgrade chart
# microk8s helm3 upgrade -f values-traefik.yaml traefik traefik/traefik
