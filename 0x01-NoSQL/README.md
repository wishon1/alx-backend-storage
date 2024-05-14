## NoSQL Specialization (0x01)

### overview
This specialization focuses on NoSQL databases, specifically MongoDB, covering various aspects such as database management, querying, insertion, updating, and deletion of data.

### Resources
- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [Mongosh](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh)

### Learning Objectives
By the end of this project, you should be able to:
- Define NoSQL and its differences from SQL
- Explain ACID principles
- Understand document storage and types of NoSQL databases
- Identify the benefits of using a NoSQL database
- Query, insert, update, and delete data in MongoDB
- Utilize MongoDB for various applications

### Requirements
#### MongoDB Command File
- All files interpreted/compiled on Ubuntu 18.04 LTS using MongoDB 4.2
- Files must end with a new line
- The first line of all files should be a comment: `// my comment`
- A `README.md` file at the root of the project folder is mandatory

#### Python Scripts
- All files interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- Files must end with a new line
- The first line of all files should be `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should follow the `pycodestyle` style (version 2.5.*)
- All modules and functions should have documentation
- Code should not execute when imported (`if __name__ == "__main__":`)

### Tasks
1. **List all databases**
    - Write a script that lists all databases in MongoDB.

2. **Create a database**
    - Write a script that creates or uses the database `my_db`.

3. **Insert document**
    - Write a script that inserts a document in the collection `school`.

4. **All documents**
    - Write a script that lists all documents in the collection `school`.

5. **All matches**
    - Write a script that lists all documents with `name="Holberton school"` in the collection `school`.

6. **Count**
    - Write a script that displays the number of documents in the collection `school`.

7. **Update**
    - Write a script that adds a new attribute to a document in the collection `school`.

8. **Delete by match**
    - Write a script that deletes all documents with `name="Holberton school"` in the collection `school`.

9. **List all documents in Python**
    - Write a Python function that lists all documents in a collection.

10. **Insert a document in Python**
    - Write a Python function that inserts a new document in a collection based on keyword arguments.

11. **Change school topics**
    - Write a Python function that changes all topics of a school document based on the name.

12. **Where can I learn Python?**
    - Write a Python function that returns the list of schools having a specific topic.

13. **Log stats**
    - Write a Python script that provides some stats about Nginx logs stored in MongoDB.
