### To demonstrate config maps:
After creating the applicationm,
1. Create the configmap by running `oc create -f sample-cm.yaml`
2. Mount the configmap by running `oc set volume dc/openshift-python-sample --add -t configmap --configmap-name=sample-cm -m /app/folder/`
