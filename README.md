### Extended Microservice Documentation
![alt text](https://github.com/hambord/CS361_Term_Project/blob/main/resources/microservice_uml.png?raw=true)

This additional microservice acts as an extension of the export functionality of the main dungeon generator application. Once an instance has been created, the user will be offered the ability to export the instance to a text file. If the user approves, the instance will be serialized in a binary format to be ran by the exporter microservice.

From here, the exporter will direct the user to import the text file. It will then deserialize the instance object (FrontData here), and offer two options: changing tiles and exporting. Changing the tiles is optional, but exporting is required. The changing tiles option changes the visual representation of the instance object, but leaves the raw data of the instance alone for compatability reasons.

PLEASE NOTE: Running the exporter will remove the serialized data from the text file. If, for any advanced reason, you need this serialized data, do not run the exporter.
