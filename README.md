# Data Engineering Project: Detection of anomalies in credit card transactions through an API from a MongoDB database using Machine Learning

## Introduction

Within the scope of activities of a data engineer, making data available or receiving data through an API is a common practice. This API can be consumed by different applications, aligning with the advantages associated with the microservices philosophy. Among others, such as improved security, efficient data abstraction, and maintenance flexibility.

In this context, this project aims to develop an API capable of detecting anomalies in credit card transactions using machine learning in a MongoDB database hosted in the Cloud of Amazon Web Services (AWS). Throughout development, good Continuous Integration and Continuous Delivery (CI/CD) practices will be incorporated, using Docker containers.

# Technologies Used
   - MongoDB: Document-oriented NoSQL database system that offers flexibility and scalability, ideal for dealing with large volumes of data and variable data structures.
   - FastApi: Python framework used for API development. It offers efficient performance and ease of development, enabling the creation of effective endpoints.
   - Python: Programming language used in the project, integrated with the FastAPI framework to implement the API logic.
   - Docker: Used to create images with the necessary libraries that will be used with Uvicorn.
   - Uvicorn: Lightweight and fast ASGI server for Python, used to host the FastAPI application, providing high performance and the ability to handle asynchronous connections.
   - AWS (Amazon Web Services): Used to host applications, manage databases (such as MongoDB), and provide computing resources, storage, and other services essential for the operation and scalability of your API and other system components.
   - Pandas: Python library for data manipulation and analysis, offering robust data structures and tools for manipulating tables and time series.
   - Scikit-learn: Python library for machine learning, providing a range of algorithms for classification, regression, clustering and dimensionality reduction.
   - SciPy: Python toolkit for math, science, and engineering, covering modules for optimization, linear algebra, integration, and more.
   - Joblib: Library used for serialization of Python objects, especially useful for saving and loading machine learning models.
   - NumPy: Fundamental library for scientific computing in Python, offering support for multidimensional arrays and tools for complex mathematical operations.
   - Pydantic: Library for data validation and management in Python, used especially to create data models with strongly typed types.

## Machine Learning Architecture

![ml_2](https://github.com/robsonsants/Credit_Card_Fraud_Detection/assets/32533017/1f17fb2d-f36f-4396-a74a-0b4148417842)

## Project Architecture

![ap1_vesta](https://github.com/robsonsants/Credit_Card_Fraud_Detection/assets/32533017/ff1a70b4-9bde-4538-8e7e-c10492d2a496)

## Project steps

1. Dataset
    
   This work uses the dataset called IEEE-CIS Fraud Detection https://www.kaggle.com/competitions/ieee-fraud-detection, which was designed to enable the construction and evaluation of detection systems of fraud in e-commerce. This dataset is made up of two main tables: the transaction table and the identity table. The transaction table contains crucial information about each transaction, including the transaction amount, the credit card used, the date and time of the transaction, as well as other relevant attributes. The identity table provides additional data about the individuals involved in transactions, including demographic characteristics and information about the devices used by users.

   The IEEE-CIS Fraud Detection dataset includes 434 attributes, of which 400 are anonymized (V1 to V339) in order to protect the privacy of users and institutions. Each row in the transaction table represents a specific electronic transaction. Each transaction has a label, which can take on two values indicating: legitimate transaction or fraudulent transaction. In this sense, the dataset can be used to build binary classifiers. As the data set is quite large and unbalanced, we only used a part of the data, more precisely a subset formed by the train_identity and the train_transaction, thus forming a new data set, which will be used in the subsequent stages of this work.

2. Docker Image Creation

    To facilitate the implementation of the API, a Dockerfile was developed. This document includes an image of Python, incorporating all essential libraries for the project, as well as the complete source code of the application. Once the container was established, a command was executed to establish a service using Uvicorn on a designated port, which allows access to the API.
    We use Docker to ensure a consistent and repeatable execution environment. This tool allows software to run reliably in different environments, simplifying development, testing and deployment.

3. Creating Machines on AWS

    The system was implemented in virtual machine instances of type t2.medium, with 2 vCPUs and 4 GB of RAM, in the São Paulo region of the Amazon Web Service (AWS) cloud. A virtual machine was allocated for each service, in addition to a virtual machine for Locust. Each service ran in a single Docker container.
   Special emphasis was placed on data held on Vesta's side, to replicate the functionality of an authentic banking application. The purpose of this was to guarantee the best possible simulation of a real banking application when running the tests.
   All of these elements work together to support the application, allowing the entire system to be started, stopped and managed conveniently, providing high efficiency and portability.

4. Experiments - testing 
    To evaluate the performance and maximum service capacity of the system, we carried out experiments using the Locust tool https://locust.io/, an open source load testing framework that allows you to simulate simultaneous actions of multiple users in one web service. During the experiments, Locust was used to capture critical metrics, such as the response time of each request and the total number of requests served. Additionally, a detailed log was kept, including the exact duration each service took to process and complete a transaction and the CPU and memory consumption of the virtual machines used. This made it possible to obtain a comprehensive view of the system's performance under load, identifying potential bottlenecks and identifying opportunities for improvement for future work.
    
   The application was subjected to experiments that varied the number of initial clients and the generation rate (i.e., number of clients started per second). 6 experiments were carried out with different configurations: using 10 clients and a generation rate of 5 clients/s; 20 clients at a rate of 10 clients/s, 30 clients at a rate of 15, 40 clients at a rate of 20, 50 clients at a rate of 25, and finally 60 clients and 30 starts per second. The duration of the experiment was maintained at 3 minutes in the 6 configurations.

   For analysis purposes, 10% of the initial requests were removed in all experiments as it was a system warm-up phase.


### Configuration 

To use the code you need to have the machine learning model trained exported to the .joblib to use in the SERVICE 4 (prediction) and the .json with the features to use on SERVICE 3 (data enricher).
