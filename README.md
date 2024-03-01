### Extended Microservice Documentation
![alt text](https://github.com/hambord/CS361_Term_Project/blob/main/resources/microservice_revised.png?raw=true)

This revised version of the microservice combines both the generator and exporter functionality into one, persistent service that persistently searches the "working" folder for serialized instance data to generate a result from. The two text files, "current_instance.txt" is a temporary file meant to jump-start the instance generation and to hand the data back to the client. This text file is deleted almost right away after the generation is finished. The second text file contains the exported version of the map, if set. It also contains all the customizing tile parameters if the user has set them.

Unlike my first milestone, generator.py is meant to run in the background at all times. It uses these two text files as a communication layer to send and recieve work. Above is a UML diagram that highlights visually this "hand off" between both generator.py and main.py.
