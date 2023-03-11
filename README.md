# Description
This is a clone of the famous AirBnB. For now, we are at the first step
consisting  of just building a***command intepreter***tailored to manage
AirBnB ojects.

#Execution*

##Interactive Mode
  $ ./console.py
  (hbnb) help

  Documented commands (type help <topic>):
  ========================================
  EOF  help  quit

  (hbnb) 
  (hbnb) 
  (hbnb) quit
  $

##Non-Interactive Mode
  $ echo "help" | ./console.py
  (hbnb)

  Documented commands (type help <topic>):
  ========================================
  EOF  help  quit
  (hbnb) 
  $
  $ cat test\_help
  help
  $
  $ cat test\_help | ./console.py
  (hbnb)

  Documented commands (type help <topic>):
  ========================================
  EOF  help  quit
  (hbnb) 
  $
The contributors to the repository:
***Mohamed SENGHOR***
