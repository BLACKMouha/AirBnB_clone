#!/usr/bin/python3
'''
Initializes a package
'''

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
