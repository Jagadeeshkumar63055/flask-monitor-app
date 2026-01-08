pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jagadeesh604/flask-monitor"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Jagadeeshkumar63055/flask-monitor-app'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
            }
        }

        stage('Push Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-creds']) {
                    sh 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }
    }
}
