pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(false)
    }

    stages {
        stage('Install dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                bat '.venv\\Scripts\\python.exe -m playwright install --with-deps chromium'
            }
        }

        stage('Run tests') {
            steps {
                bat 'if not exist reports mkdir reports'
                bat 'if not exist allure-results mkdir allure-results'
                bat 'if not exist traces mkdir traces'
                bat 'if not exist screenshot mkdir screenshot'
                bat '.venv\\Scripts\\python.exe -m pytest --junitxml=reports/junit.xml --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/junit.xml', allowEmptyResults: true
            archiveArtifacts artifacts: 'reports/**/*,allure-results/**/*,traces/**/*,screenshot/**/*', allowEmptyArchive: true
        }
    }
}