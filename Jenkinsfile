pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'echo "Construyendo..."'
            }
        }
        
        stage('Test') {
            steps {
                bat 'echo "Testeando..."'
            }
        }
        
        stage('Generate Documentation') {
            steps {
                // Este comando usa Doxygen en Windows
                bat 'doxygen Doxyfile'
            }
        }
        
        stage('Version Control') {
            steps {
                // Verificamos que se creó la carpeta docs
                bat 'dir docs'
            }
        }
        
        stage('Deploy') {
            steps {
                bat 'echo "Desplegando..."'
            }
        }
    }
}

// Version final para Windows 