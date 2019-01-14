# GameLoop on AsyncIO

Proof of Concept - created during hackathon.

This project was targeted to solve one of problems that we have encountered. Thanks 
to it we could connect WWW server that would serve gamepad written in React to Game
Engine without using any extra component than just internal memory. This has greatly
reduced delays in connection.
  
## Requirements

This project was created for Python 3.7. All required libraries can be installed
via `pip` and are placed in `requirements.txt` file.

## How to install

For easier bootstrap of this project I suggest using [Docker](https://www.docker.com/) containers.

### Docker
Just type this command in main directory:

```commandline
$ docker build -t gameloop .
$ docker run -it --rm gameloop
```

## Credits
Author of this project is Adam Strojek