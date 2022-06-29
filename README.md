## Deployment Dockerized webapp onto aws Elastic Beanstalk 
For deployment of our dockerized system i followed the path of utilising travis CI which is a CI/CD tool for continuous integration. 
In travis.yml ist the testing and building and deploying of our container app defined with details to the specific Container information useful for deployment on elasticbeanstalk being contained in the Dockerrun.json
Our dockerized app was successfully deployed by travis CI but had a few shortcommings while being deployed on elastic beanstalk .
The two major issues were as a result of working with a docker-compose.yml instead of a Dockerfile
- Replicating the Volume on which our db(postgress) would need , and since pgadmin and celeryworker depended on the db we would only have a handfull of our dockers running 
- Questions at to how Network as defined in the docker-compose.yml should be implemented also arrise
