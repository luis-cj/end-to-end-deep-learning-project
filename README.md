# End-to-end Deep Learning project

This repository presents an end-to-end project deep learning project. An image classifier is used to evaluate whether a chicken is infected with a disease or not.

The main steps are the following:

- Develop the project in a Jupyter Notebook
- Implement the data pipelines with Python scripts using OOP guidelines
- Write an application locally that takes a new image as an input to the model and makes a prediction
- Create a Docker Image of the application
- Upload the Docker Image to the Docker Hub
- Connect the Docker Image to AWS ECR
- Run the application from an AWS ECS instance


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml