pipeline {
        agent any

        stages {

                stage('SonarQube analisys') {
                steps {
                withSonarQubeEnv('SonarQube') {
                sh "/var/lib/jenkins/tools/sonar-scanner/bin/sonar-scanner -Dsonar.projectKey=python-project"
                                }
                        }
                }

                stage('Deploy hello world') {
                        steps{
                             sh "python3 helloWorld.py"

                                        }
                                }
                stage('Deploy Hours2Sec'){
                        steps{
                                sh 'python3 hours2sec.py'
                        }
                }
                

                        }
                }
