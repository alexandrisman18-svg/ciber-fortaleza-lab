pipeline {
    agent any

    stages {
        stage('Preparación') {
            steps {
                // Descarga el código del repositorio
                checkout scm
            }
        }

        stage('QA con PyBuilder') {
            steps {
                echo 'Iniciando auditoría de calidad...'
                // MODIFICACIÓN: Ejecutamos PyBuilder (pyb) en lugar de python test.py
                // Esto asegura que se cumplan los umbrales de cobertura y flake8
                sh 'pyb'
            }
        }

        stage('Construcción de Imagen') {
            steps {
                echo 'Creando imagen de Docker...'
                sh 'docker build -t bioguard-image:latest .'
            }
        }

        stage('Despliegue Seguro') {
            steps {
                echo 'Desplegando en puerto seguro...'
                // MODIFICACIÓN: Eliminamos el contenedor viejo si existe y lanzamos el nuevo
                // Usamos el puerto 8443 solicitado por el CISO
                sh '''
                docker rm -f bioguard-app || true
                docker run -d -p 8443:5000 --name bioguard-app bioguard-image:latest
                '''
            }
        }
    }
    
    post {
        success {
            echo '¡Misión cumplida! El pipeline ha finalizado con éxito.'
        }
        failure {
            echo 'El pipeline ha fallado. Revisa los tests o el formato de código.'
        }
    }
}