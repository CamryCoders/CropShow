from flask import Flask,jsonify
from flask_cors import CORS
from src.routes.crop_routes import crop_routes

def create_app():
    app=Flask(__name__)

    CORS(app,
         origins=["http://localhost:5173"])
    app.register_blueprint(
        crop_routes,
        url_prefix="/api/crop"
    )
    # Test the server
    @app.route("/test",
        methods=["POST"]
    )
    def crop_recommend():
        return {
            "message":"route and server is working"
        }
    

    return app
app=create_app()