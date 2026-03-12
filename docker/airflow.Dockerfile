FROM apache/airflow:2.9.1

USER root

RUN pip install \
    pandas \
    kafka-python \
    scikit-learn \
    prophet \
    mlflow \
    feast

USER airflow

WORKDIR /opt/airflow

COPY pipelines/airflow_dags /opt/airflow/dags

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False

EXPOSE 8080