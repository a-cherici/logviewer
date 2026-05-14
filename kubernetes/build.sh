docker login -u admin -p "${NEXUS_PASSWD}" docker-project-snapshot.alm-repos.sogei.it

docker build -t docker-project-snapshot.alm-repos.sogei.it/automation/logviewer:0.0.1 --build-arg HTTPS_PROXY=http://26.0.148.5:80 -f Dockerfile ..
docker push docker-project-snapshot.alm-repos.sogei.it/automation/logviewer:0.0.1

docker logout