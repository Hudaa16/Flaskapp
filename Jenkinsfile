pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main', url: 'https://github.com/Hudaa16/Flaskapp.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                bat 'pytest tests/'
            }
        }
        stage('Build') {
            steps {
                echo 'Building application...'
                bat 'echo Build completed'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Simulating deployment...'
                bat 'mkdir C:\\flask-deploy 2>nul'
                bat 'echo Deployment successful > C:\\flask-deploy\\deploy.log'
            }
        }
    }
}