from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_identity
from models import db
from config import Config
from flasgger import Swagger
from routes.auth_routes import auth_routes
from routes.movie_routes import movie_routes
from routes.room_routes import room_routes
from routes.seat_routes import seat_routes
from routes.tickets_route import ticket_routes
from routes.showtime_routes import showtime_routes
from routes.cinema_routes import cinema_routes
from routes.payments_routes import payment_routes
from routes.combo_routes import combo_routes
from routes.ticket_type_routes import ticket_type_routes
from routes.user_routes import user_routes
from flask_cors import CORS
from sqlalchemy import text

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  

    CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

    # ---------------------------
    # JWT CONFIG
    # ---------------------------
    app.config["JWT_SECRET_KEY"] = app.config.get("JWT_SECRET_KEY", "super-secret-key")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = app.config.get("JWT_ACCESS_TOKEN_EXPIRES", 3600)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = app.config.get("JWT_REFRESH_TOKEN_EXPIRES", 86400)

    # ---------------------------
    # SWAGGER CONFIG
    # ---------------------------
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/swagger/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/swagger/static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
    }

    # Dùng chuẩn Swagger 2.0
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Cinema Management API",
            "description": "API documentation for the Flask backend (Auth, Movie, Room, Cinema, etc.)",
            "version": "1.0.0",
            "contact": {
                "name": "Doan Hoai Viet",
                "email": "yashinwaa@gmail.com"
            }
        },
        "basePath": "/",  # quan trọng: giúp Swagger nhận đúng prefix
        "schemes": ["http"],  # hoặc https nếu deploy
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
            }
        },
        "security": [{"Bearer": []}],
    }

    # Tạo Swagger instance
    Swagger(app, config=swagger_config, template=swagger_template)

    # ---------------------------
    # Init extensions
    # ---------------------------
    db.init_app(app)
    jwt = JWTManager(app)

    # ---------------------------------
    # Middleware kiểm tra JWT
    # ---------------------------------
    @app.before_request
    def check_jwt():
        open_prefixes = [
            "/auth/login",
            "/auth/signup",
            "/auth/forgot-password",
            "/auth/refresh",
            "/apidocs",
            "/static",
            "/swagger",
            "/movie",
            "/ticket",
            "/cinema",
            "/"
        ]
        if any(request.path.startswith(prefix) for prefix in open_prefixes):
            return
        try:
            verify_jwt_in_request()
            request.user = get_jwt_identity()
        except Exception as e:
            return jsonify({"error": "Unauthorized", "message": str(e)}), 401

    # ---------------------------------
    # Register blueprints
    # ---------------------------------
    app.register_blueprint(auth_routes, url_prefix="/auth")
    app.register_blueprint(movie_routes, url_prefix="/movie")
    app.register_blueprint(room_routes, url_prefix="/room")
    app.register_blueprint(seat_routes, url_prefix="/seat")
    app.register_blueprint(ticket_routes, url_prefix="/ticket")
    app.register_blueprint(ticket_type_routes, url_prefix="/ticket-type")
    app.register_blueprint(showtime_routes, url_prefix="/showtime")
    app.register_blueprint(cinema_routes, url_prefix="/cinema")
    app.register_blueprint(payment_routes, url_prefix="/payment")
    app.register_blueprint(combo_routes, url_prefix="/combo")
    app.register_blueprint(user_routes, url_prefix="/user")

    @app.route("/")
    def home():
        return "Flask backend with SQLAlchemy + JWT + Swagger is ready!"
    
    @app.route("/seed", methods=["POST"])
    def run_seed():
        from seed_data import seed_data
        seed_data(app)
        return {"message": "Seed completed!"}


    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

