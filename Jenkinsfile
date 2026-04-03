pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    reuseNode true
                }
            }
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    reuseNode true
                }
            }
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t flask-cicd .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying app...'
                sh '''
                    docker stop flask-cicd-app || true
                    docker rm flask-cicd-app || true
                    docker run -d \
                        --name flask-cicd-app \
                        -p 5001:5000 \
                        flask-cicd
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! App is live at http://localhost:5001'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}