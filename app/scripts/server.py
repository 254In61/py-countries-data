"""
- Server module
- Server receives a query from client.
- Based on type of request received from client, server queries the mysql db server in the backend
"""
# Run from the root
# $ python3 -m app.scripts.server 
# To be extended to include search based on City or Leader.

from flask import Flask, request, jsonify
from app.modules.db import query_db

app = Flask(__name__)

@app.route('/countries/<country_name>', methods=['GET'])
def get_all_countries(country_name):
    # country = request.args.get('country_name')
    # query = f"SELECT * FROM countries WHERE name = {name}"
    
   
        
    try:
        if country_name.lower() == "all":
            query = "select * from countries"

            # for row in query_db(query):
            #     print(row)

        else:
            query = f"select * from countries where country = '{country_name}'"
            # print(query_db(query))

        return jsonify(query_db(query))
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Error handling
        
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)
    # the run() method of Flask class runs the application on the local development server.
    # Once started, it is continous until stopped ( CTRL+C , or is there another way??)
    # including debug, there will be a print out of any changes plus auto-updates and auto-restarts
    # Defining host='0.0.0.0' to listen to all connections
