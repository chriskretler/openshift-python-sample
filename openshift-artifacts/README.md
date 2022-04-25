To use cert-manager with a route, you must request a certificate first. The certificate specifies which issuer will be used to request the certificate. The route annotation:

```
cert-utils-operator.redhat-cop.io/certs-from-secret: demo-route-secret
```

Tells the cert-utils-operator to use the secret that was previously created by cert-manager that contains the certificate.

For the route, issue these commands:
```
oc create -f demo-cert.yaml
oc create -f demo-route.yaml
```

To use cert-manager with an ingress, just create the ingress. The annotation on the ingress specifies which issuer to use when requesting the certificate:

```
cert-manager.io/cluster-issuer: letsencrypt
```

For the ingress, just issue this command:
```
oc create -f demo-ingress.yaml
```
