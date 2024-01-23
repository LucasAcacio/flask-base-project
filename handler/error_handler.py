from flask import jsonify, make_response, current_app as app

'''
    Custom error handling
'''

class ErrorHandler():
    def handle_server_error(e):
        response = jsonify({
                'message': e.description,
                'name': e.name,
                'status': e.code
            })
        
        app.logger.error(response.json)
        return make_response(response, e.code)

    def handle_user_error(e):
        response = jsonify({
                'message': e.description,
                'name': e.name,
                'status': e.code
            })
        
        app.logger.warn(response.json)
        return make_response(response, e.code)