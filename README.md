# Apache-Airflow
Project to house code for apache-airflow instance in docker with 4 workers.  Instance uses Celery to excecute tasks in parallel, Redis as the messaging queue to route tasks from the scheduler to the workers, and PostgreSQL as a backend database for both the Airflow instance and Celery.  All docker containers are run via docker-compose.
