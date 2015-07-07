#AWS Elastic Beanstalk
Collection of codes and docs related to AWS Elastic Beanstalk during my studies

## Notes

### Features

* Integrated with CloudWatch, ELB and AS
* Preconfigured stacks (.NET, PHP, Ruby, Python, Tomcat, Node.js, Docker, Go)
* Multiple tier building blocks: Web-LB, Single Instance, Worker Tier
* Multiple client types: AWS Console, EB CLI, AWS CLI, VisualStudio, Eclipse, SDK's

all environments have the "use rds" option, when you go your env to create the db layer, it sends some variables to your instance, with user, dburl, password, inside the variables.

### Limitations


eb deploy (creates versioning of files while deploying, which can be accessed through console on "Application versions"

hrk2
Th3Lif3R&+051110*v


-=- Beanstalk Homework -=-

- Create a python env using flask, creating an elastic cache during deploy and cache some specific folder inside the memcache

- Create a php env, change the memory_limit and post_max_size from php.ini (how the fuck am I going to do it? which one is the best one? tip: ebextensions ;)

- In one of the two env above, add http keepalive on the ELB that runs behind it (always using container_commands inside the ebextensions)

- Create an env with RDS and make it work with flask