post_validator = {
      "$jsonSchema": {
         "bsonType": "object",
         "required": [ "title", "content" , "author",],
         "properties": {
            "title": {
               "bsonType": "string",
               "description": "must be a string and is required"
            },
            "content":{
               "bsonType": "string",
               "description": "must be a string and is required"
            },
            "author_id":{
                "bsonType": "objectId",
               "description": "must be a string and is required"
            }
            }
         }
      }

user_validator = {
      "$jsonSchema": {
         "bsonType": "object",
         "required": [ "username", "email", "password", "user_group" ],
         "properties": {
            "username": {
               "bsonType": "string",
               "uniqueItems": "true",
               "maxlength":24,
               "description": "must be a string and is required"
            },
            "email":{
               "bsonType": "string",
              "uniqueItems": "true",
              "pattern" : "^.+@.+$",
               "description": "must be a string and is required"
            },
            "password":{
               "bsonType": "string",
               "minLength":8,
               "maxLength":32,
               "description": "must be a string and is required and shoul be between 8 to 32 characters"

            },
            "user_group" :{
              "enum":["Admin", "Teacher", "Student"],
              "description":"have to choose one from these"

            }
            
            }
         }
      }

