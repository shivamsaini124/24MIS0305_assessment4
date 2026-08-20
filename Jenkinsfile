pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Starting Jenkins Pipeline'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m pip install --user pytest'
            }
        }

        stage('Banking Loan QA') {
            steps {
                sh 'python3 -m pytest test_loan.py -v'
            }
        }

        stage('E-Commerce QA') {
            steps {
                sh 'python3 -m pytest test_ecommerce.py -v'
            }
        }

        stage('Hospital QA') {
            steps {
                sh 'python3 -m pytest test_hospital.py -v'
            }
        }

        stage('Airline QA') {
            steps {
                sh 'python3 -m pytest test_airline.py -v'
            }
        }

        stage('Parking QA') {
            steps {
                sh 'python3 -m pytest test_parking.py -v'
            }
        }

    }

    post {
        success {
            echo 'All QA tests passed successfully!'
        }

        failure {
            echo 'Some QA tests failed!'
        }
    }
}