from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/store_rating', methods=['POST'])
def store_rating():
    try:
        data = request.get_json()
        rating = data['rating']
        
        # Store the rating in Redis
        redis_client.rpush('ratings', rating)
        
        return jsonify({"message": "Rating stored successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_ratings', methods=['GET'])
def get_ratings():
    try:
        # Retrieve all ratings from Redis
        ratings = redis_client.lrange('ratings', 0, -1)
        
        return jsonify({"ratings": ratings})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)