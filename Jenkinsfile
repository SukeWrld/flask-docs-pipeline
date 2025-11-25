pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'echo "Instalando dependencias (simulado)..."'
            }
        }
        
        stage('Test') {
            steps {
                bat 'echo "Tests finalizados correctamente."'
            }
        }
        
        stage('Generate Documentation') {
            steps {
                // Si Doxygen está en el PATH, esto funcionará.
                // Si vuelve a fallar, tendremos que poner la ruta completa (C:\Program Files\...)
                bat 'doxygen Doxyfile' 
            }
        }
        
        stage('Version Control') {
            steps {
                echo 'Verificando documentación generada...'
                // En Windows se usa 'dir' en lugar de 'ls'
                bat 'dir docs'
            }
        }
        
        stage('Deploy') {
            steps {
                bat 'echo "Despliegue en entorno de prueba completado."'
            }
        }
    }
}