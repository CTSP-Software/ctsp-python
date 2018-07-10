#!/usr/bin/env groovy

pipeline{
    agent any
    stages{
        stage('Build'){
            steps {
                sh 'echo "Building... (maybe not needed)"'
                sh 'ls'
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