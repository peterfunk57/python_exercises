pipeline {
        agent any

        stages {

                stage('SonarQube analisys') {
                steps {
                withSonarQubeEnv('SonarQube') {
                sh "/var/jenkins_home/tools/sonar-scanner//bin/sonar-scanner"
                                }
                        }
                }

                stage('Deploy') {
                        steps{
                             sh "python3 helloWorld.py"

                                        }
                                }
                        }
                }
