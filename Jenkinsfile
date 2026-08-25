pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(false)
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
                sh '.venv/bin/python -m playwright install --with-deps chromium'
            }
        }

        stage('Run tests') {
            steps {
                sh 'mkdir -p reports allure-results traces screenshot'
                sh 'xvfb-run -a .venv/bin/python -m pytest --junitxml=reports/junit.xml --alluredir=allure-results'
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
