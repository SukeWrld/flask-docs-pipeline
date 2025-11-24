pipeline {
    agent any

    stages {
        stage('Instalar dependencias') {
            steps {
                sh 'python -m venv venv'
                sh './venv/Scripts/pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                sh './venv/Scripts/python -m pytest test_app.py'
            }
        }

        stage('Generar documentación') {
            steps {
                sh 'doxygen docs/Doxyfile'
            }
        }
    }
}
