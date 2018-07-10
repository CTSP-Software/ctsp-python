pipeline{
    agent any
    stages{
        stage('Build'){
            steps {
                sh 'echo "Building... (maybe not needed)"'
            }
        }
        stage('Test'){
            steps{
                sh 'echo "Testing..."'
            }
        }
        stage('Deploy'){
            steps{
                sh 'echo "Deploying..."'
            }
        }
    }
    post {
        always {
            echo 'Build done'
        }
        success {
            echo 'SUCCESSFULL build!'
        }
        failure {
            echo 'Failed.'
        }
        changed {
            echo 'You got it this time.'
        }
    }
}