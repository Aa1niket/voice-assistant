pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        
        
        stage('Run Voice Assistant') {
            steps {
                sh 'python assistant.py'
            }
        }
    }
}
