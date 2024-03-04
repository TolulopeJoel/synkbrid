# Remote Collaborate API Documentation

Welcome to the API documentation for Remote Collaborate. This document provides detailed information about the API endpoints and how to use them.

## Table of Contents

- [Authorization](#authorization)
  - [User Login](#user-login)
  - [User Registration](#user-registration)
  - [Refresh Token](#refresh_token)
- [Tasks](#tasks)
  - [Get All Tasks](#get-all-tasks)
  - [Create a Task](#create-a-task)
  - [Get a Task](#get-a-task-by-id)
  - [Update a Task](#update-a-task)
  - [Partially Update a Task](#partially-update-a-task)
  - [Delete a Task](#delete-a-task)
- [Teams](#teams)
  - [Get All Teams](#get-all-teams)
  - [Create a Team](#create-a-team)
  - [Get a Team](#get-a-team-by-id)
  - [Update a Team](#update-a-team)
  - [Partially Update a Team](#partially-update-a-team)
  - [Delete a Team](#delete-a-team)

## Authorization

Before accessing most of the API endpoints, you need to obtain an authorization token by using the following endpoints:

### User Login

- **URL**: `/api/auth/login/`
- **HTTP Method**: POST
- **Description**: Log in to your account and obtain an authorization token.

#### Request

- **Request Headers**:
  - `Content-Type`: application/json

- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  - Response Status: `200 OK`
- **Response Body**:
    ```json
    {
    "access_token": "your_access_token",
    "refresh_token": "your_refresh_token"
    }
    ```


### User Registration

- **URL**: `/api/auth/register/`
- **HTTP Method**: POST
- **Description**: Register a new user account.

#### Request

- **Request Headers**:
  - `Content-Type`: application/json

- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  - Response Status: `201 Created`

### Refresh Token

- **URL**: `/api/auth/token/refresh/`
- **HTTP Method**: POST
- **Description**: Get new access token.

#### Request

- **Request Headers**:
  - `Content-Type`: application/json

- **Request Body**:
  ```json
  {
    "refresh_token": "your_refresh_token",
  }
  ```
- **Response**:
  - Response Status: `200 OK`
- **Response Body**:
    ```json
    {
    "access_token": "your_access_token",
    }
    ```

## Tasks

### Get All Tasks
- **URL**: `/api/tasks/`
- **HTTP Method**: GET
- **Description**: 
#### Request

- **Request Headers**:
  - `Content-Type`: application/json

- **Response**:
  - Response Status: `200 OK`
- **Response Body**:
  ```json
  {
    "count": 123,
    "next": "http://api.example.org/accounts/?page=4",
    "previous": "http://api.example.org/accounts/?page=2",
    "results": [
      {
        "id": 0,
        "name": "string",
        "description": "string",
        "assignees": [
          {
            "id": 0,
            "username": "string",
            "first_name": "string",
            "last_name": "string"
          }
        ],
        "start_date": "2019-08-24T14:15:22Z",
        "due_date": "2019-08-24T14:15:22Z",
        "status": "not-started"
      }
    ]
  }
  ```

### Create A Task


- **URL**: `/api/tasks/`
- **HTTP Method**: POST
- **Description**: Create a new task.

#### Request

- **Request Headers**:
  - `Content-Type`: application/json

- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string",
    "start_date": "2019-08-24T14:15:22Z",
    "due_date": "2019-08-24T14:15:22Z",
    "status": "not-started"
  }
  ```
- **Response**:
  - Response Status: `201 Created`

- **Response Body**:
  ```json
  {
    "id": 0,
    "name": "string",
    "description": "string",
    "assignees": [
      {
        "id": 0,
        "username": "string",
        "first_name": "string",
        "last_name": "string"
      }
    ],
    "start_date": "2019-08-24T14:15:22Z",
    "due_date": "2019-08-24T14:15:22Z",
    "status": "not-started"
  }
  ```
