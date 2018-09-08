pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'INFO: Build'
        sh '''#/bin/bash

# DEBUG
id
printenv | sort
#
which python || true
which pip || true
which python3 || true
which pip3 || true
#
which docker || true
which docker-compose || true
# docker --version
# docker-compose --version
# docker-compose build --pull

# EOF'''
      }
    }
    stage('Test') {
      steps {
        sh 'python3 manage.py shell'
      }
    }
  }
}
