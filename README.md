# pizzeria-zenduty
Technical Assignment - Zenduty<br>
[A Pizzeria Application]

## Note

Due to technical issues like errors, it was not possible to create asynchronous tasks. I tried ***background_tasks*** and ***celery*** and both libraries were unsuccesfull. I have implemented the use-case in a more manual way.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/arjunshen0y/pizzeria-zenduty.git
```
# Switch Branch to Master and Go to Project Directory
```sh
$ git checkout master
$ cd pizzeria-zenduty/Pizzeria
```

Since the requirement was to run the whole app with a single Docker command:

```sh
$ docker-compose up -d
```

## Some Snippets

# Add a Pizza
![Screenshot 2023-09-07 210508](https://github.com/arjunshen0y/pizzeria-zenduty/assets/44999908/4f7f713f-3c88-40e0-b769-1f862ad25f6c)

# View the Order
![Screenshot 2023-09-07 211752](https://github.com/arjunshen0y/pizzeria-zenduty/assets/44999908/810b7655-8748-4c5b-ac0f-ea0cbd91a776)

# Order Status Changing

https://github.com/arjunshen0y/pizzeria-zenduty/assets/44999908/fd70213f-8baf-4270-b7fd-e73de6c305f5
