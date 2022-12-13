## How to use this repository

______

Before going through the use of this repo, you have to make sure gpu set in your environment.

To run this repository, follow the steps below:

1. first you clone the repository.
>$ git clone https://github.com/Yvan-BM/fr-boris-gptj.git

2. move into the main directory
>$ cd fr-boris-gptj

3. Install all dependencies (It is recommended to create a virtual environment before)
>$ pip install -r requirements.txt 

4. Now you can launch the flask server. For this you have two options.
    - You can run a simple python command
        >$ python3 app.py
    - You can use docker instead
        >$ docker build -t YOUR-CONTAINER-NAME .

        >$ docker run YOUR-CONTAINER-NAME

At this step your flask app is deployed and you can test it. In another terminal you run following command.
>$ python3 test.py

You can modify the input prompt in the `test.py` file and play around.