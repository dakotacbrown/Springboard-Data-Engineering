# Springboard Data Engineering Capstone 1

This is the repository for Dakota Brown's Springboard Data Engineering Capstone 1

# Prerequisites

1. [docker](https://docs.docker.com/get-docker/) (docker-compose will be needed as well).
2. [AWS account](https://aws.amazon.com/) to set up cloud services.
3. [Install](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) AWS CLI on an EC2 instance.
4. [Configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) AWS CLI on an EC2 instance.
5. [Visualization](https://public.tableau.com/app/profile/dakota.cheyenne.brown/viz/Capstone1Visualization_16604991072950/HealthCarein2009vs2019) Data visualization can be found here.
6. [Slide Deck](assets/slides.pdf) Slide deck explaining the project can be found here.

# Design

![ETL Design](assets/images/architecture.png)

# Entity Relationship Diagram

![Entity Relationship Diagram](assets/images/wbERD.png)

# Data

[WHO medical data through the world bank.](https://data.worldbank.org/)


# Setup and run

If this is your first time using AWS, make sure to check for the IAM roles `EMR_EC2_DefaultRole` and `EMR_DefaultRole`.

```bash
aws iam list-roles | grep 'EMR_DefaultRole\|EMR_EC2_DefaultRole'
# "RoleName": "EMR_DefaultRole",
# "RoleName": "EMR_EC2_DefaultRole",
```

If the roles not present, create them using the following command

```bash
aws emr create-default-roles
```

Create an S3 bucket and load the scripts (located in code) into into a folder named scripts. 
Create a raw and transformed folder as well.

To start up airflow on your EC2 instance:

```bash
docker-compose -f docker-compose-LocalExecutor.yml up -d
```
(You can exchange LocalExecutor for CeleryExecutor as well)

Remove `-d` to see everything start up and view any errors if needed.

go to [http://localhost:8080/admin/](http://localhost:8080/admin/) and turn on the `who_data` DAG. You can check the status at [http://localhost:8080/admin/airflow/graph?dag_id=who_data](http://localhost:8080/admin/airflow/graph?dag_id=who_data). 

![DAG](assets/images/dag_design.png)

In EC2, make sure you're able to access the port airflow is bound to. The photo below helped me, however you would have to allow
public traffic to EMR or it would block the creation of the an EMR instance from EC2.

![Airflow fix.](assets/images/emr_rules.png)

# Terminate local instance

```bash
docker-compose -f docker-compose-LocalExecutor.yml down
```



