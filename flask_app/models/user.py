from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friendship

class User:
    def __init__( self , data ):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('friendships_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('friendships_schema').query_db( query, data )
    
    
    
    @classmethod
    def get_user(cls, data):
        query = "SELECT * from users where id = %(id)s;"
        results = connectToMySQL('friendships_schema').query_db(query, data)
        return cls(results[0])
    
    
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, created_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('friendships_schema').query_db(query, data)
    
    @classmethod
    def delete_user(cls, data):
        query = "DELETE from users where id = %(id)s;"
        return connectToMySQL('friendships_schema').query_db(query, data)
    
    
    
    @classmethod
    def get_user_with_friends(cls, data):
        query = "SELECT * from users LEFT JOIN friendships on users.id = friendships.user_id LEFT JOIN users as user2 on users2.id = friendships.friend_id where users.id = %(id)s;"
        results = connectToMySQL("friendships_schema").query_db(query, data)
        
        user = cls(results[0])
        
        if len(results) > 0:
            return True
        
        return user
    
    
    
    
    
    
    # @classmethod
    # def unselected_user(cls, data):
    #     query = "SELECT * from users where users.id NOT IN (SELECT user_id from friendships where friend_id = %(id)s);"
        
    #     results = connectToMySQL("friendships_schema").query_db(query, data)
    #     user = []
    #     for row in results:
    #         user.append(cls(row))
    #     return user