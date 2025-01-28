from flask import Flask, Response, request, jsonify, make_response

"""
    * "request" module from flask is used to access incoming data from HTTP requests (like form data, query strings, or JSON payloads).
    * Acts as the API provider to handle incoming HTTP requests on the server-side
"""

items: list[dict[str, str | int]] = [{
    'id': 1,
    'name': 'Item 1',
    'description': 'This is item 1'
},
    {
        'id': 2,
        'name': 'Item 2',
        'description': 'This is item 2'
}]
app: Flask = Flask(__name__)

# 1> GET call - directly fetch entire list by hitting the route
@app.route('/items', methods=['GET'])
def get_items() -> Response:
    return jsonify(items)                            # return items also works


# 2> GET call - fetch the particular list item i.e, dict by inserting the item_id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_an_item(item_id: int) -> Response:

    # 1st check if item_id exists in items dict
    for item in items:
        if item.get('id') == item_id:
            return jsonify(item)
    return make_response(jsonify({
        'Error': 'Item not found'
    }), 404)


# 3> POST call - adds a new item to the items list
@app.route('/items', methods=['POST'])
def create_item() -> Response:

    # Gets the JSON payload from the request body
    add_item: dict[str, int | str] = request.get_json()


    for key in ('id', 'name', 'description'):           # () is a tuple coz of 1st brackets
        if key not in add_item:                         # 1> Valdiates if the payload structure is right
            return make_response(jsonify({
                'Error': 'Invalid payload structure, key names missed'
            }), 400)
 
        if key == 'id' and any(item['id'] == add_item['id']       # 2> Generator Expression inside any(): Checks if item with the entered "id" already exits
                               for item in items):
            return make_response(jsonify({
                'Error': f'The id: {add_item['id']} already exists, insert a different id'
            }), 409)       

    # adds an item to the existing list named "items"
    items.append(add_item)

    # provide confirmation payload after successful addition - 201 created
    return make_response(jsonify({
        'message': 'Item Added Successfully',
        'item': add_item
    }), 201)


# taken down logic:
    # 1> Valdiates if the payload structure is right
        # if not all(key in add_item
        #         for key in ("id", 
        #                         "name", 
        #                         "description")):
        #     return jsonify({
        #             'Error': 'Invalid payload structure'
        #             })

    # 2> Checks if item with the entered "id" already exits
        # for item in items:
        #     if item['id'] == add_item['id']:
        #         return jsonify({
        #             'Error': f'The id: {item['id']} already exists, insert a different id'
        #         })


# 4> PUT call - updates an existing item in the items list
@app.route('/items/<int:item_id>', methods = ['PUT'])
def update_item(item_id: int) -> Response:

    update_item: dict[str, int | str] = request.get_json()                  # "update_item" is the same dict I'm passing as request payload / body

    for item in items:
        if item['id'] == item_id:
            item.update(update_item)                            # updating existing dictonary "item" from top with my POSTMAN payload / body
            return jsonify({
                'message': 'Item updated',
                'item': item
            })

    return make_response(jsonify({
        'Error': f'Item: {item_id} not found'
        }), 404)


# To hell with optimization:
# def update_item(item_id: int) -> Response:
#     update_item: dict[str, int | str] = request.get_json()

#     # Find the item to update
#     item = next((item for item in items if item['id'] == item_id), None)

#     if item is None:
#         return make_response(jsonify({'Error': 'Item not found'}), 404)

#     # Update the item with new data
#     item.update(update_item)

#     return make_response(jsonify({
#         'message': 'Item Updated Successfully', 
#         'item': item
#         }), 200)


# 5> DELETE call - updates an existing item in the items list
@app.route('/items/<int:item_id>', methods = ['DELETE'])
def delete_item(item_id: int) -> Response:
    global items

    # optimized code - where in I'm re-updating my original list named "items" with all dict whose key do not matches with deleted item_id
    items = [item for item in items 
             if item['id'] != item_id]
    return make_response(jsonify({
        'message': 'item successfully deleted'
        }), 200)
    
    # boiler-plate code
    # for i in range(len(items)):
    #     if items[i]['id'] == item_id:
    #         del items[i]
    #         return make_response(jsonify({
    #             'message': 'item successfully deleted'
    #         }))

    # return make_response(jsonify({
    #     'Error': 'There is no such item'
    # }), 404)



if __name__ == '__main__':
    app.run(debug=True, port = 3100)
