# AirBnB clone project

## Description
The goal of this project is to deploy a simplified copy of the AirBnB website.
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
$
Documented commands (type help <command>):
========================================
EOF   all   count   create   destroy   help   quit   show

$
$ cat test_help
help
$
$ cat test_help | ./console.py
$
Documented commands (type help <command>):
========================================
EOF   all   count   create   destroy   help   quit   show

$
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
(hbnb) create <class>
(hbnb)
(hbnb) all [<class>]
(hbnb) <class>.all()
(hbnb)
(hbnb) count [<class>]
(hbnb)
(hbnb) show <class> <id>
(hbnb) <class>.show("<id>")
(hbnb)
(hbnb) destroy <class> <id>
(hbnb) <class>.destroy("<id>")
(hbnb)
(hbnb) update <class> <id> <key> <value>
(hbnb) <class>.update("<id>", {"<key1>"=<value1>, "<key2>"="<value2>", ..., "<keyn>"=<valuen>})
```
