from flask import Blueprint,redirect,render_template,url_for,flash,request
from .. import db
from ..models import Task
from flask_login import login_required,current_user

task_bp = Blueprint('task',__name__)

@task_bp.route("/view_task")
@login_required
def view_task():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.id).all()
    return render_template('tasks.html',tasks=tasks)

@task_bp.route("/add_task",methods=["GET","POST"])
@login_required
def add_task():
    title = request.form.get('title')
    if title:
        new_task=Task(title=title,user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash("Task added Successfully!","success")
    else:
        flash("Please enter the task!","danger")
    return redirect(url_for("task.view_task"))

@task_bp.route("/toggle_status/<int:task_id>",methods=["POST"])
@login_required
def toggle_status(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task:
        if task.status == "Pending":
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Completed"
        else:
            task.status="Pending"
        db.session.commit()
    else:
        flash("Task Not found!","danger")

    return redirect(url_for("task.view_task"))

@task_bp.route("/delete_task",methods=["POST"])
@login_required
def delete_task():
    tasks = current_user.tasks
    if tasks:
        for task in tasks:
            db.session.delete(task)
        db.session.commit()
        flash("Deleted Successfully!","success")
    else:
        flash("No task found!","danger")
    
    return redirect(url_for("task.view_task"))
