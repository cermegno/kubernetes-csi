# kubernetes-csi
Supporting files for a Docker, Kubernetes and CSI training lesson
## Topics
The goal of the training is to get deeper understanding of the different aspects of storage management in Kubernetes. In order to do that, the module assumes that the student has little to no knowledge of Docker. Thus an introduction to Docker is provided

After that the training covers:
- Kubernetes
- Dynamic storage provisioning with the CSI driver
- Volume Snapshots with CSI
- Quotas for storage resources
- Storage limits

The labs have been tested with the DellEMC XtremIO CSI driver:

[https://github.com/dell/csi-xtremio-deploy](https://github.com/dell/csi-xtremio-deploy)

The training uses also 2 containers images from Docker Hub:
- docker pull cermegno/myfirstcontainer
- docker pull cermegno/simplog
