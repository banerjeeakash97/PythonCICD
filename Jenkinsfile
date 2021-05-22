pipeline {
    agent any

    stages {
        stage('Git Checkout') {
            steps {
                git credentialsId: 'f47c1088-e82c-48dc-86ca-0c21000c05d5', url: 'https://infygithub.ad.infosys.com/DNA/PythonCICD.git'
                echo "Git checkout Completed"
            }
        }
        stage('Build') {
            steps {
                sh 'python test_name_function.py'
            }
        }        
    }
}
