pipeline {
    agent any
	/*environment {
		PATH = \ect\usr\bin\
	}*/
 

    stages {
        stage('Git Checkout') {
            steps {
                git credentialsId: '4cdb5638-1e76-443c-af1d-a155d81f3d13', url: 'https://infygithub.ad.infosys.com/DNA/PythonCICD.git'
                echo "Git checkout Completed"
            }
        }
        stage('Build1') {
			when {
                branch 'master' 
            }
            steps {
                //sh 'python pip install xmlrunner'
                sh 'python test_name_function.py'
            }
        }
        stage('Unit tests') {
			when {
                branch 'master' 
            }
            steps {
                bat "pytest mytest.py --junitxml=test-reports.xml"
            }
            post {
                always {
                    junit 'test-reports.xml'
                }
            }
        }
        stage('Coverage') {
			when {
                branch 'Develop' 
            }
            steps {
                echo "Code Coverage"
                sh  ''' coverage run irisvmpy/iris.py 1 1 2 3
                        python -m coverage xml -o ./reports/coverage.xml
                    '''
            }
            post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'reports/coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])
                }
            }
        }
    }
}
