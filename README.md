# ***Project***

## Todo App Backend API with User-Specific Tasks

## ***Description***

Develop a Backend API for a Todo application using Python, integrating MongoDB as the database. Implement Auth0 for authentication, ensuring that Todos are user-specific, and users can only modify their tasks. Deploy the application on Google Cloud Services, using MongoDB Atlas for the database and Google App Engine for the API. Demonstrate the API endpoints with a Postman collection.

## ***Requirements***

   ### 1. API Development:
   * Use Python (FastAPI) for backend development.
   * Implement CRUD operations for Todos, ensuring that these operations are user-specific:
     * **Create**: Users can add new todos.
     * **Read**: Users can fetch a list of their todos and a single todo by ID.
     * **Update**: Users can update their todos by ID.
     * **Delete**: Users can remove their todos by ID.
   * Each Todo item should have at least the following fields: id,title, description, status, and due_date. It is up to you to set up the user data and 
     how each todo is linked to its user.
   * Implement user registration and login endpoints.
   ### 2. Database:
   * Use MongoDB for storing data. Structure the database schema to associate Todos with Users appropriately.
   * Utilize MongoDB Atlas for hosting the database.
   ### 3. Authentication:
   * Implement Auth0 for secure authentication. See [Auth0](https://auth0.com/)
   * Secure all API endpoints using JWT tokens provided by Auth0, ensuring that users can only access and modify their todos.
   ### 4. Deployment:
   * Deploy the API on Google App Engine.
   * Ensure the database is accessible via MongoDB Atlas.
   ### 5. Testing & Documentation:
   * Provide a Postman collection that covers all API endpoints, demonstrating CRUD operations for todos, user-specific access, authentication flow, and 
     error handling.
   * Include a README file with:
     * Instructions on how to set up and run the project locally.
     * Steps to deploy the project on Google Cloud Services.
     * A brief description of the API endpoints and how to use them, emphasizing the user-specific functionality.
## ***Deliverables***
   * Source code for the backend API.
   * Postman collection file.
   * README documentation.


# ***Implementation***

## ***Technology Stack***
   1. Python (FastAPI)
   2. MongoDB Atlas
   3. Postman Collections
   4. Google App Engine

## ***Installation***

   * **To Setup the project dependencies _LOCALLY_**

     1. Create a virtual environment for the project dependencies using this command:

        * **On Linux:**
           ```bash
           $ sudo pip install virtualenv
           ```
           ```bash
           $ python3 -m venv todo-env                  # here the created virtual environment is named 'todo-env' but you can you any name you want
           ```
        * **On Windows:**
           ```bash
           > pip install virtualenv
           ```
           ```bash
           > python -m install todo-env
           ```
     2. Activate the virtual environment using this command:

        * **On Linux:**
            ```bash
            $ source todo-env/bin/activate
            ```
        * **On Windows:**
            ```bash
            > cd todo-env
            ```
            ```bash
            > Scripts\activate
            ```

     3. Clone this repo using this command from your terminal:

        ```bash
        $ git clone https://github.com/ahmeds26/Todo-Backend-API.git
        ```
    
     4. Install the dependencies by running the requirements.txt file using this command:

        * **On Linux:**
            ```bash
            $ sudo pip install -r requirements.txt
            ```
        * **On Windows:**
            ```bash
            > pip install -r requirements.txt
   
   * **To Configure MongoDB Atlas Cluster**

     1. Follow the steps in this link [MongoDB Atlas](https://www.mongodb.com/docs/atlas/tutorial/create-atlas-account/) to create a MongoDB Atlas account.

     2. Create a MongoDB Atlas Cluster by following steps in this link [Atlas Cluster](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/)

     3. Make sure to copy the **connection string** called **Atlas URI** as we need it to connect to the MongoDB Cluster.

   * **To Handle _MongoDB Cluster_ Environment Variables**

     1. Create a **.env** file in the root of the project folder.

     2. Add these environment variables to the **.env** file as follows:

        * MONGO_ATLAS_URI=<YOUR_ATLAS_URI>                                              ```# the cluster connection string obtained in the setup of MongoDB```
        * DATABASE_NAME=<YOUR_MAIN_DATABASE>                                            ```# Name of database```
        * USERS_COLLECTION=<YOUR_USERS_COLLECTION>                                      ```# Name of users' collection```
        * TASKS_COLLECTION=<YOUR_TASKS_COLLECTION>                                      ```# Name of tasks' collection```

   * **To Implement _Auth0_ Authorization**

     1. Create a free Auth0 account by signing up through this link [Auth0](https://auth0.com/signup)

     2. Create an API on your Auth0 Dashboard:

        * **Name** of the API can be any name you want.
        * **Identifier** could be your FastAPI Root endpoint for example here <http://localhost:8000/api>
        * **Signing Algorithm** keep it as it is **RS256**

   * **To Handle _Auth0_ Environment Variables**

     1. Create a **.env.development** file in the root of the project folder.
     
     2. Add these environment variables to the **.env.development** file as follows:

        * AUTH0_DOMAIN=your.domain.auth0.com                                         ```# Can be found on Auth0 application Dashboard```
        * AUTH0_API_AUDIENCE=https://your.api.audience                               ```# Can be found on Auth0 application Dashboard```
        * AUTH0_ISSUER=https://your.domain.auth0.com/                                ```# Can be found on Auth0 application Dashboard```
        * AUTH0_ALGORITHMS=RS256                                                       ```# Can be found on Auth0 application Dashboard```

   
   * **To Run the project _LOCALLY_**

     * Run the following command from the project directory:

        ```bash
        $ python main.py
        ```
     * The API endpoints are served on **_Local Host_** at this URL **<http://localhost:8000/docs>**

   * **To Test the API using _Postman Collection_**

     * You can make **Postman Tests** from the collection file in the project root or from utilizing the collection link 
       [Postman Collection](https://documenter.getpostman.com/view/16619415/2sA3kSo3Up#641cfeb3-56ba-492e-af11-083f38acc288)

