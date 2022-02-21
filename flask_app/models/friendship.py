from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friendship:
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = ["user_id"]
        self.friend_id = ["friend_id"]
        self.user_first_name = data['user_first_name']
        self.user_last_name = data['user_last_name']
        self.friend_first_name = data['friend_first_name']
        self.friend_last_name = data['friend_last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    
    @classmethod
    def add_frienship(cls, data):
        query = "INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES (%(user_id)s, %(friend_id)s , NOW(), NOW());" # this returns an id
        return connectToMySQL("friendships_schema").query_db(query, data)
    
    
    
    @classmethod
    def get_friendship(cls, data):
        query = "SELECT users.first_name as user_first_name, users.last_name as user_last_name, friendships.*, users2.id, users2.first_name as friend_first_name, users2.last_name as friend_last_name from users LEFT JOIN friendships on users.id = friendships.user_id LEFT JOIN users as users2 on users2.id = friendships.friend_id where user_id = %(user_id)s and friend_id = %(friend_id)s;" # as key word : the new column name has to be in the __init__ to be accessed.
        results = connectToMySQL('friendships_schema').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    
    
    
    @classmethod
    def get_all_user_friendships(cls):
        query = "SELECT users.first_name as user_first_name, users.last_name as user_last_name, friendships.*, users2.id, users2.first_name as friend_first_name, users2.last_name as friend_last_name from users LEFT JOIN friendships on users.id = friendships.user_id LEFT JOIN users as users2 on users2.id = friendships.friend_id;"
        results = connectToMySQL("friendships_schema").query_db(query)
        friendships = []
        for row in results:
            friendships.append(cls(row))
        return friendships
    
    
    
    
    
    @classmethod
    def update_friendship(cls, data):
        query = "UPDATE friendships SET user_id = %(user_id)s, friend_id = %(friend_id)s, created_at = NOW(), updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('friendships_schema').query_db(query, data)
    
    @classmethod
    def delete_friendship(cls, data):
        query = "DELETE from friendships where id = %(id)s;"
        return connectToMySQL('friendships_schema').query_db(query, data)
    
    
    
    
    # created a friendship class and remove the freiend class
    
    
    # @classmethod
    # def unfavored_friends(cls, data):
    #     query = "SELECT * from users where users.id NOT IN (SELECT user_id from friendships where friend_id = %(id)s);"
        
    #     results = connectToMySQL("friendships_schema").query_db(query, data)
    #     user = []
    #     for row in results:
    #         user.append(cls(row))
    #     return user