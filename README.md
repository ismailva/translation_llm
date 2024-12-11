## Translation Application

- This application consists of two modules:
    - A FastAPI server running on port 8080
    - A Streamlit UI running on port 8501

- You can access the FastAPI documentation at [http://localhost:8080/docs](http://localhost:8080/docs).
- Follow the steps below to create and run this application:
    - Create an OpenAI key from the website and set it as an environment variable named `openai_key`.
    - Navigate to the directory where the code is located.
    - Execute the command: `docker build -t translation_app .`
    - To run the container, use the following command: `docker run -p 8080:8080 -p 8501:8501 -e openai_key=$openai_key translation_app`
- For evaluating quality of output use notebook named as evaluation.ipynb
    - I have created three evaluation method and bert based method is most effective (bert-base-multilingual-cased)
