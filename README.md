# end-to-end-SMS-Spam-classifier

```bash
## Workflows
1. Update config.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
9. Update the dvc.yaml
```

## Steps

- git clone the repo from github

- define the template of the project

- define setup.py

- create env

```bash
conda create -n sms-env python=3.9 -y
conda activate sms-env
```

- define requirements.txt

```bash
pip install -r requirements.txt
```

- define logging and utils

- **Data Ingestion**

- **EDA and go through the project in jupyter notebook**

- **Data Validation**

- **Data Transformation**

- **model training**

- **Model Evaluation**

    - Adding mlflow

    ```bash
    MLFLOW_TRACKING_URI=https://dagshub.com/fraidoon_omarzai/end-to-end-SMS-Spam-classifier.mlflow \
    MLFLOW_TRACKING_USERNAME=fraidoon_omarzai \
    MLFLOW_TRACKING_PASSWORD=bc25b16bd5206328d8899cf34377f26ad71d1420 \
    python script.py


    # run in cmd windows
    %env:MLFLOW_TRACKING_URI="https://dagshub.com/fraidoon_omarzai/end-to-end-SMS-Spam-classifier.mlflow"
    $env:MLFLOW_TRACKING_USERNAME="fraidoon_omarzai"
    $env:MLFLOW_TRACKING_PASSWORD="bc25b16bd5206328d8899cf34377f26ad71d1420"

    # run in mac/linux
    export MLFLOW_TRACKING_URI=https://dagshub.com/fraidoon_omarzai/end-to-end-SMS-Spam-classifier.mlflow
    export MLFLOW_TRACKING_USERNAME=fraidoon_omarzai 
    export MLFLOW_TRACKING_PASSWORD=bc25b16bd5206328d8899cf34377f26ad71d1420
    ```

- using `streamlit` to create a web page for our project

- **Docker**

    - adding code to docker file
    - bulid the docker image
    ```bash
    docker build -t sms-app .
    docker ps
    docker images
    ```
    - running our app using docker

    ```bash
    docker run -p 8080:8080 sms-app
    htpp://localhost:8080
    ```

- create .github/workflows/cicd.yaml


###############**AWS Section**################

1. Login to AWS console
2. Create IAM user for deployment and download the project_accessKeys

```bash
#with specific access
1. ECR: Elastic Container registry to save your docker image in aws
2. EC2 access : It is virtual machine


#Description: About the deployment
1. Build docker image of the source code (already done)
2. Push your docker image to ECR
3. Launch Your EC2 
4. Pull Your image from ECR in EC2
5. Lauch your docker image in EC2

#Policy for IAM:
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

```
3. Create ECR repo to store/save docker image
```bash
- Save the URI: 851725628730.dkr.ecr.eu-west-2.amazonaws.com/sms
```
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
```bash
#optinal
sudo apt-get update
sudo apt-get upgrade -y

#required
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
6. Configure EC2 as self-hosted runner:
```bash
setting-->actions-->runner-->new self hosted runner--> choose os--> copy each command and run it on EC2 Instance Connect
```
7. Setup github secrets:
```bash
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION = eu-west-2
AWS_ECR_LOGIN_URI = 851725628730.dkr.ecr.eu-west-2.amazonaws.com/sms
ECR_REPOSITORY_NAME = sms
```