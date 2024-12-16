# So you can't work because you're in a different cafe with a different ip range for metallb?

 - create a configmap for metallb if there's not one there and add the range of the cafe you're in

```touch metallb-configmap.yaml```

then add
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: metallb-config
  namespace: metallb-system
data:
  config: |
    address-pools:
    - name: default
      protocol: layer2
      addresses:
      - 192.168.1.100-192.168.1.250 # previous range
      - 192.168.5.100-192.168.5.250 # previous range
      - 192.168.XX.100-192.168.XX.250 # new cafe range
```

apply it

```
microk8s kubectl apply -f metallb-configmap.yaml
```

refresh the certificates on microk8s

```
sudo microk8s.refresh-certs --cert ca.crt
```

check the configmap is applied

```
microk8s kubectl get configmap metallb-config -n metallb-system -o yaml
```

you should be good to go!