# Topics to Learn
- [ ] How to use Git
- [ ] VirtualBox & Vagrant
- [ ] Agile Planning
- [ ] Unittest
- [ ] Creating a CI/CD pipeline
- [ ] Docker
- [ ] Infrastructure as code / deploying to cloud (AWS)


# Resmo

It is to build the `/users` resource.


## Prerequisite Installation using Vagrant

Download [VirtualBox](https://www.virtualbox.org/)

Download [Vagrant](https://www.vagrantup.com/)

Clone the project to your development folder and create your Vagrant vm

```
    $ git clone https://github.com/IJaykkk/resmo.git
    $ cd resmo
    $ vagrant up
```

## Access Flask

In the vm, run

```
    $ vagrant ssh
    $ cd /vagrant
    $ python run.py
```

## Run test

In the vm, run
```
    $ vagrant ssh
    $ cd /vagrant
    $ nosetests
```
it will show the test result and coverage rate

## API Docs.

### User 
#### Add a new user

```Bash
```

return : user_id

Create a new user with username, 'panda', and unhashed passwords, "pass".

#### Get a token

```Bash
```
return : user token

Retrieve a token for user login.

#### Read a user

```Bash
```

return : user_id

Retrieve user information given username and password.





### List Resources 

1. `/users`

    Use this URL to GET the list of all user resources.

2. Example:
```
    curl -X GET http://0.0.0.0:5000/users
```

### Read a Resource
1. `users/{id}`

    Use this URL to retrieve a user with specific `{id}`.

2. Example:
```
    curl -X GET http://0.0.0.0:5000/users/1
```

### Create a Resource 
1. `/users`

    Use this URL to send POST request.

2. Example:
```
    curl -d '{"email": "example@exmaple.com"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/users
```
### Update a Resource
1. `/users/{id}`

    Use this URL to update an existing entry in our resources where the user id is `{id}`

2. Example:
```
    curl -d '{"email": "test@test.com"}' -H "Content-Type: application/json" -X PUT http://0.0.0.0:5000/users/1
```
### Delete a Resource
1. `/users/{id}`

    Use this URL to DELETE the user resources which satisfied the id equals to `{id}`

2. Example
```
    curl -X DELETE http://0.0.0.0:5000/users/1
```

### Query Resources by some attribute of the Resource
1. `/users?query1=value&query2=value`

    Use this URL to GET the user resources which satisfied all the query conditions.

2. Example:
```
    curl -X GET "http://0.0.0.0:5000/users?email=foo@bar.com"
```

## Shutdown
When you are done, you can use the `exit` command to get out of the virtual machine just as if it were a remote server and shut down the vm with the following:

```
    $ exit
    $ vagrant halt
```

If the VM is no longer needed you can remove it with from your computer to free up disk space with:
```
    $ vagrant destroy
```
