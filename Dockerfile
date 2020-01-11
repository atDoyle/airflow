FROM puckel/docker-airflow
ENV AIRFLOW_HOME=/usr/local/airflow
COPY ./requirements.in /usr/local/airflow/requirements.in
RUN pip install --user pip-tools
ENV PATH=$PATH:/usr/local/airflow/.local/bin
RUN pip-compile /usr/local/airflow/requirements.in
RUN pip install --user -r requirements.txt
COPY ./config/* /usr/local/airflow/