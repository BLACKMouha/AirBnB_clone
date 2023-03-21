# AirBnB clone project

## Description
The goal of this project is to deploy a simple of the AirBnB website.
The first step is to build a command intepreter to manipulate data without
visual interface, like in a Shell (perfect for debugging and development).
The interface is called The Console. For now, the console is able to
create, delete and update an object (basemodel class and its subclasses).
But, it can also persists them in a JSON file. This file is used to save
and reload data whenever we want.

## Usage:

In interactive mode
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <command>):
========================================
EOF   all   count   create   destroy   help   quit   show

(hbnb)
(hbnb)
(hbnb) quit
$
```
In non-interactive mode
```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <command>):
========================================
EOF   all   count   create   destroy   help   quit   show

(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <command>):
========================================
EOF   all   count   create   destroy   help   quit   show

(hbnb)
$
```
Classes defined
---------------
- BaseModel
- User
- Place
- State
- City
- Amenity
- Review

```bash
$ create <class>
$
$ all [<class>]
$ <class>.all()
$
$ count [<class>]
$
$ show <class> <id>
$ <class>.show("<id>")
$
$ destroy <class> <id>
$ <class>.destroy("<id>")
$
$ update <class> <id> <key> <value>
$ <class>.update("<id>", {"<key1>"=<value1>, "<key2>"="<value2>", ..., "<keyn>"=<valuen>})
```
