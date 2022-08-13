pipeline {
  agent any
  stages {
    stage('Build'){
      steps {
        sh 'pip install -r requirements.txt' 
      }
    }
    stage('Test'){
      steps {
        echo 'python3 manage.py test --settings=todos.settings.prod'
      }
    }
    stage('Deploy') {
      steps { 
        sh 'ssh johndoe@192.168.56.105 -oStrictHostKeyChecking=no \
        git pull \
        cd cicd_django \
        sudo systemctl restart nginx \
        sudo systemctl restart gunicorn'
      }
    }
  }
}