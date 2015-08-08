#AWS Elastic Beanstalk
Collection of codes and docs related to AWS Elastic Beanstalk during my studies

## Notes

### Features

* Integrated with CloudWatch, ELB and AS
* Preconfigured stacks (.NET, PHP, Ruby, Python, Tomcat, Node.js, Docker, Go)
* Multiple tier building blocks: Web-LB, Single Instance, Worker Tier
* Multiple client types: AWS Console, EB CLI, AWS CLI, VisualStudio, Eclipse, SDK's
* All environments have the "use rds" option when you go your env to create the db layer, it sends some variables to your instance, with user, dburl, password, inside the variables, to be used in your code

### Limitations

### Tips and A-HA moments

* To use a "Ref" into the custom option "Files" of ebextensions, you need to use the "`" character. It's not documented anywhere. Found it in this blog post: http://blogs.aws.amazon.com/application-management/post/Tx2PM64E771CQGG/Using-DynamoDB-and-SNS-with-Elastic-Beanstalk-in-any-Supported-AWS-Region
* Files added to folder "/opt/elasticbeanstalk/hooks/appdeploy/post/" of the instances will get executed automatically after the environment creation is complete, so that's a good way to run scripts on the environment by simply creating them through ebextensions ("files" option)

## EB CLI

### Features

* Integrates with Git to create the repo, but "eb deploy" commands is used to push (like "git push") the code to the EB instance

### Commands

* eb deploy (creates versioning of files while deploying, which can be accessed through console on "Application versions")
* eb use (select the default env to be used)
* eb open (runs a browser with the application url. However, if you have "links" text-browser installed when deploying from a linux box, it will open it in "links")
