## Python JSON conversion table

| JSON 	        | Python| 
|:--------------|:-------|
| object       	| dict   |
| array 	    | Number | 
| string 	    | str 	 | 
| number (int) 	| int 	 | 
| number (real) | float  | 
| true 	        | True 	 | 
| false 	    | False  | 
| null 	        | None 	 | 

## JSON Syntax
The syntax of JSON is straightforward. It is built on top of two simple structures:

* A collection of ``name/value pairs`` (in Python, they are represented as a Python dictionary).
````JSON
{
    "name": "James",
    "gender": "male"
    "age": 32
}
````
* An ordered list of values.
````JSON
{"name":"James","gender":"male","age":32}
````

## JSON Constraints
JSON format has several constraints:

* The ``name`` in ``name/value`` pairs must be defined as a string in double quotes ``(")``.
* The ``value`` must be of the valid JSON data type:
    * **String** – several plain text characters
    * **Number** – an integer
    * **Object** – a collection of JSON ``key/value`` pairs
    * **Array**  – an ordered list of values
    * **Boolean**– true or false
    * **Null**   – empty object
* Valid JSON object can’t contain other data types, for example, ``datetime``

## Working With Python JSON Module
``JSON`` is a standard data exchange format used by many programming languages, including ``Python``. ``JSON`` (JavaScript Object Notation) represents data in a human-readable text format and is easy for computers to process. Python provides a built-in module called JSON to work with JSON data. 
> The ``JSON`` module **allows you to convert Python objects into JSON strings and back up again**. It also provides methods for loading and saving ``JSON`` files.

In addition, the ``json`` module **can also be used to convert Python dictionaries into JSON objects**, it contains methods for processing JSON data, including the following operations: 
* parsing
* serializing
* deserializing
* encoding
* decoding
* pretty-printing. 

Overall, the ``json`` module makes it easy to work with JSON data in Python programming language.


## Some usefull links
 * [Python JSON – Complete Tutorial](https://hands-on.cloud/python-json-module-examples/)

 * [Python JSON Parsing using json.load() and loads()](https://pynative.com/python-json-load-and-loads-to-parse-json/)

 * [JSON.DUMP(S) & JSON.LOAD(S)](https://www.bogotobogo.com/python/python-json-dumps-loads-file-read-write.php)