pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                // Install Python dependencies, if needed
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Voice Assistant') {
            steps {
                sh 'python voice_assistant.py'
            }
        }
    }
}
