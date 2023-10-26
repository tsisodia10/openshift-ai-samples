import redis

# Connect to the Redis server
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Specify the key where ratings are stored
ratings_key = 'ratings'

# Use the LRANGE command to retrieve all ratings
ratings = redis_client.lrange(ratings_key, 0, -1)

# Check if ratings were retrieved
if ratings:
    print("Stored Ratings:")
    for rating in ratings:
        print(rating.decode('utf-8'))  # Decode bytes to a string
else:
    print("No ratings found in Redis.")
