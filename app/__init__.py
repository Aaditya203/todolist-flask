from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
login_manager = LoginManager()



def create_app():
    app=Flask(__name__)
    app.config["SECRET_KEY"]="dev"
    app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:1234@localhost:5432/todo_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view='auth.login'
    @login_manager.user_loader
    def load_user(user_id):
        # import here to avoid circular import at module import time
        from .models import Users
        return Users.query.get(int(user_id))
    # routes add krenge baad me

    from .routes.auth import auth_bp
    from .routes.task import task_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    with app.app_context():
        db.create_all()

    return app

