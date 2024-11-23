import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
# 1. Save Data with Hash
def save_hash_data():
    # Save data for user 1
    user1_data = {'name': 'Alice', 'age': '30', 'city': 'New York'}
    for key, value in user1_data.items():
        r.hset('user:1', key, value)
     #Save data for user 2
    user2_data={'name':'Rajni','age':'35','city':'Ujjain'}
    for key,value in user2_data.items():
        r.hset('user:2',key,value)
    #Save Data for user 3
    user3_data={'name':'deepak','age':'37','city':'Indore'}
    for key,value in user3_data.items():
        r.hset('user:3',key,value)

    print("Data save successfully!")

def fetch_all_user_data():
    user1=r.hgetall('user:1')
    user2=r.hgetall('user:2')
    user3=r.hgetall('user:3')
    print(f"User 1 Data:  {user1}")
    print(f"User 2 Data:  {user2}")
    print(f"User 3 Data:  {user3}")

    #for get Specific data Or fied name

    user1_name=r.hget('user:1','name')
    user2_age=r.hget('user:2','age')
    user3_city=r.hget('user:3','city')

    print(f"User 1 Name:{user1_name}")
    print(f"User 2 Age:{user2_age}")
    print(f"User 3 City:{user3_city}")

save_hash_data()
fetch_all_user_data()