microk8s helm3 repo add jenkinsci https://charts.jenkins.io/
microk8s helm3 repo update
microk8s helm3 install -f values-jenkins.yaml jenkins jenkinsci/jenkins --version 5.7.21
