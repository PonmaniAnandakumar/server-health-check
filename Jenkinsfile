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

    post {
        unstable {
            emailext(
                to: 'ponmanianandakumar9363@gmail.com',
                subject: 'WARNING: Server Health Check',
                body: '''WARNING: The server health check detected a WARNING condition.

Please check the Jenkins console output for CPU, Memory and Disk usage.

Jenkins Job: ${JOB_NAME}
Build Number: ${BUILD_NUMBER}
Build URL: ${BUILD_URL}
'''
            )
        }

        failure {
            emailext(
                to: 'ponmanianandakumar9363@gmail.com',
                subject: 'CRITICAL: Server Health Check',
                body: '''CRITICAL: The server health check detected a CRITICAL condition.

Please check the Jenkins console output for CPU, Memory and Disk usage.

Jenkins Job: ${JOB_NAME}
Build Number: ${BUILD_NUMBER}
Build URL: ${BUILD_URL}
'''
            )
        }
    }
}