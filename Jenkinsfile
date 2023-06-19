pipeline {
    agent any
    tools{
        maven 'maven_3_5_0'
    }
    }
        stages {
            stage('Build Flask App') {
                steps {
                    git branch: '*/main', url: 'https://github.com/JibinKoshy07/py-flask-mysql'  // Replace "your-repo-url" with your actual repository URL
                    sh 'pip install -r requirements.txt'  // Assuming your Flask app has a requirements.txt file
                }
            }
            // Add more stages for testing, deployment, etc. if needed
        }
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t javatechie/devops-integration .'
                }
            }
        }
        stage('Push image to Hub'){
            steps{
                script{
                   withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhubpwd')]) {
                   sh 'docker login -u javatechie -p ${dockerhubpwd}'

}
                   sh 'docker push javatechie/devops-integration'
                }
            }
        }
        stage('Deploy to k8s'){
            steps{
                script{
                    kubernetesDeploy (configs: 'deploymentservice.yaml',kubeconfigId: 'k8sconfigpwd')
                }
            }
        }
    }
}