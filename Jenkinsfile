pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/ganesh-gowda/jenkins-py.git', branch: 'main'
            }
        }
        stage('average'){
            steps{
                bat 'C:\\Python312\\python.exe average_grades.py'
            }
        }
    }
}
