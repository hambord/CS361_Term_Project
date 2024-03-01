### Extended Microservice Documentation
![alt text](https://github.com/hambord/CS361_Term_Project/blob/main/resources/microservice_revised.png?raw=true)

This revised version of the microservice combines both the generator and exporter functionality into one, persistent service that persistently searches the "working" folder for serialized instance data to generate a result from. The two text files, "current_instance.txt" is a temporary file meant to jump-start the instance generation and to hand the data back to the client. This text file is deleted almost right away after the generation is finished. The second text file contains the exported version of the map, if set. It also contains all the customizing tile parameters if the user has set them.

Unlike my first milestone, generator.py is meant to run in the background at all times. It uses these two text files as a communication layer to send and recieve work. Above is a UML diagram that highlights visually this "hand off" between both generator.py and main.py.

To use the generator service, you must use main.py as an entry point. Setting up instance parameters are required, but the exporter parameters are options (but highly recommended.) If using the application in an advanced capacity, you must use the FrontData dataclass as the intended way to interface with the generator service. Like in the main.py version, required parameters in FrontData are those required to generate the map itself. The exporter parameters are optional here as well.

You can use either way to send data to the service, but you will always recieve (in a permanent capacity) just one generated map instance object. You can also recieve a text file with the generated and customized result, should you require one and set the parameters. This will always render to the root directory of main.py.
