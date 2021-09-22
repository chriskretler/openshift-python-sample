## Openshift Django Sample

This is a minimal [Django 3](http://www.djangoproject.com) project that you can use as the starting point to develop your own and deploy it on an [OpenShift](https://github.com/openshift/origin) cluster.

The steps in this document assume that you have access to an OpenShift cluster that you can deploy applications on.  Instructions for University of Michigan employees can be found here: https://tinyurl.com/y9gmudj6


### Local development

To run this project in your development machine, follow these steps:

1. Fork this repo and clone your fork:

  `git clone https://github.com/chriskretler/openshift-python-sample.git`

2. Build the docker image:

  `docker build -t django-ex src/`

3. Run the docker image:

  `docker run -it -p 8000:8000 django-ex`

4. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.


### Deploying to OpenShift

To follow the next steps, you need to be logged in to an OpenShift cluster and have either `admin` or `edit` in a valid project

You can use the oc command like to create your application:

`oc new-app https://github.com/chriskretler/openshift-python-sample.git --context-dir=src`

Your application will be built and deployed automatically. If that doesn't happen, you can debug your build:

`oc get builds`\
take build name from the command above\
`oc logs build/<build-name>`

And you can see information about your deployment too:

`oc describe dc/openshift-python-sample`

In the web console, the overview tab shows you a service, by default called "openshift-python-sample", that encapsulates all pods running your Django application. You can access your application by browsing to the service's IP address and port.  You can determine these by running

`oc get svc`


### Building using Cloud Native Buildpacks and Deploying to Openshift

Login to OpenShift and either via podman or docker to the associated registry. Then:
```
pack build registry.aws-np.web.umich.edu/<your namespace name>/pack-heroku --builder heroku/buildpacks --path=src/ --publish
oc new-app -i pack-gcr
oc expose dc pack-gcr
oc expose svc pack-gcr --hostname=<some hostname>.webplatformsnonprod.umich.edu
```

### Logs

By default your Django application is served with gunicorn and configured to output its access log to stderr.
You can look at the combined stdout and stderr of a given pod with this command:

`oc get pods`         # list all pods in your project\
`oc logs <pod-name>`

This can be useful to observe the correct functioning of your application.
