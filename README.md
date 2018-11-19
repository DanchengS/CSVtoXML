# CSVtoXML
A Command Line Interface that adapting Pascal-voc-writer.
generate XML file for each jpg picture base on CSV file. 


### Usage:
```sh
$ python ./CSVtoXML/CSVtoXML.py convert CSVFILEPATH PICFOLDERPATH XMLFOLDERPATH
```
Note:  
	./CSVtoXML/CSVtoXML.py is where CSVtoXML.py located. 
	CSVFILEPATH is where the CSV file located. 
	PICFOLDERPATH is the path to the folder that contains the pictures. (current directory by default)
	XMLFOLDERPATH is the path to the folder that XML files will be saved to. (current directory by default)


### Example 1:
```sh
$ cd Desktop
$ python ./Python_Other/CSVtoXML/CSVtoXML.py convert ./Python_Other/sample.csv ./Python_Other/jpg/ ./Python_Other/xml/
```

### Example 2:
If on the directory of all jpg files and wants to save xml files to the same folder
```sh
$ python ./CSVtoXML/CSVtoXML.py convert ./csvFolder/sample.csv
```


### Library used:
https://github.com/AndrewCarterUK/pascal-voc-writer





