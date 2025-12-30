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
                bat 'echo "Build completed"' 
            } 
        } 
 
        stage('Deploy') { 
            steps { 
                echo 'Simulating deployment...' 
                bat 'if not exist "C:\\flask-deploy" mkdir "C:\\flask-deploy"' 
                bat 'echo "Deployment successful!" 
            } 
        } 
    } 
 
    post { 
        success { 
            echo '?? Pipeline completed successfully! All 5 stages passed.' 
        } 
    } 
} 
