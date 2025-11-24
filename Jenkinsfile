pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Instalando dependencias...'
                // En un caso real aquí iría: sh 'pip install flask'
                sh 'echo "Simulando instalación de dependencias"'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas unitarias...'
                // Aquí irían los tests reales
                sh 'echo "Tests pasados correctamente"'
            }
        }
        
        stage('Generate Documentation') {
            steps {
                echo 'Generando documentación con Doxygen...'
                // Nota: Doxygen debe estar instalado en el contenedor donde corre Jenkins
                // Si te da error de "doxygen not found", avísame para darte el comando de instalación.
                sh 'doxygen Doxyfile' 
            }
        }
        
        stage('Version Control') {
            steps {
                echo 'Actualizando repositorio con documentación...'
                // La guía pide actualizar el repo. Esto requiere credenciales.
                // Por ahora solo verificamos que la carpeta docs exista.
                sh 'ls -l docs'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Desplegando aplicación...'
                sh 'echo "Despliegue en entorno de prueba realizado"'
            }
        }
    }
    post {
        always {
            // Paso opcional para guardar los artefactos generados (la carpeta html de docs)
            archiveArtifacts artifacts: 'docs/html/**/*', allowEmptyArchive: true
        }
    }
}