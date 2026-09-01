pipeline {
    agent any

    stages {

        stage('Run Health Check') {
            steps {
                script {

                    def exitCode = bat(
                        script: 'C:\\Users\\Shitra\\AppData\\Local\\Python\\bin\\python.exe health_check.py',
                        returnStatus: true
                    )

                    if (exitCode == 2) {
                        currentBuild.result = 'FAILURE'
                        error('Server status: CRITICAL')
                    }

                    else if (exitCode == 1) {
                        currentBuild.result = 'UNSTABLE'
                        echo 'Server status: WARNING'
                    }

                    else {
                        echo 'Server status: HEALTHY'
                    }
                }
            }
        }
    }
}