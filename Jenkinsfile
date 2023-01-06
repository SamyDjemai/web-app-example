pipeline {
                          agent any
                            environment {  
                            registry = "docker.io/snehalahire123" 
                            registryCredential = 'dockerhub' 
                             dockerImage = ''
                                                 }
            stages {
                         stage('Hello') {
                                     steps {
                                               echo 'Hello World'
                                               }
                                               }
                         stage('git clone') {
                                              steps {
                                         git credentialsId: 'github', url: 'https://github.com/ahiresnehal/web-app-example.git'
                                                sh 'ls'
                                                sh 'pwd'
                                                        }
                                                        }
            
      /*  stage('Docker Build and Tag') {
                                              steps {
                                                   //sh 'docker build -t nginxt:1.2 .' 
                                                     //sh 'docker build -t demo2:latest .' 
                                                     //sh 'docker tag demo2 snehalahire123/demo2:1.2'
                                                     //sh 'docker tag nginxte snehalahire123/nginxte:$BUILD_NUMBER'
                                                
                                                sh 'docker build -t mynewapp .'
                                                 sh 'docker tag mynewapp snehalahire123/mynewapp'
                                                 //sh 'docker tag mynewapp snehalahire123/mynewapp:$BUILD_NUMBER'
                                                       }
                                                       }
        stage('Publish image to Docker Hub') {
                                                          steps {
                                                             withDockerRegistry([ credentialsId: "dockerhub", url: "" ]) {
                                                             sh 'docker push snehalahire123/mynewapp'
                                                              //sh 'docker push snehalahire123/mynewapp:$BUILD_NUMBER' 
                                                              }
                                                              }
                                                              }
              /* stage('deploy to rancher') {
                                     steps {
                                               echo 'continuous deployment'
                                       withKubeConfig([credentialsId: 'rancher',
                    //caCertificate: '<ca-certificate>',
                    serverUrl: 'https://3.109.117.88/k8s/clusters/c-8c5n5',
                    //contextName: '<context-name>',
                    //clusterName: '<cluster-name>',
                    //namespace: '<namespace>'
                    ]) {
      sh 'kubectl apply -f /var/lib/jenkins/workspace/Final/deploymentservice.yaml'
      sh 'kubectl get pods'
    }
            }
                     }*/
              
              
              stage('deploy to rancher') {
                                     steps {
                                               echo 'continuous deployment'
                                       withKubeConfig([credentialsId: 'testconfig'])
       {
     
         //sh 'kubectl get pods'
         sh 'kubectl apply -f deploymentservice.yaml'
                                       }
                                     }
              }
              
              
       //stage('deploy to rancher') {
         //echo 'deployment'
         //withKubeConfig([credentialsId: 'rancherkubeconfig', serverUrl: 'https://3.109.117.88']) {
         //sh 'kubectl apply -f /var/lib/jenkins/workspace/Final/deploymentservice.yaml'
         //sh 'kubectl get pods'
         //}
       //}
              */
              
  }
  }
