# toast-dp-k8s-2019
Our repo for hackathon

Test Test

# HOWDOI

### Publish new version of code
Build new docker image
`docker image build . -t csv-maker:v1.1`

Tag with ecr URI
`docker tag csv-maker:v1.1 645643289692.dkr.ecr.us-east-1.amazonaws.com/csv-maker:v1.1`

Push to ecr
`docker push 645643289692.dkr.ecr.us-east-1.amazonaws.com/csv-maker:v1.1`

Update deployment.yml with the new version

Apply new version
`kubectl apply -f deployment.yml`
