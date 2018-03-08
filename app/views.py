from flask import render_template, request, redirect, url_for, abort
from app import models
from app import app, member_store, post_store

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts = post_store.get_all())


@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))

    else:
        return render_template("topic_add.html")

@app.route("/topic/update/<int:id>", methods = ["GET", "POST"])
def topic_update(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)

    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        post_store.update(post)
        return redirect(url_for("home"))

    elif request.method == "GET":
        return render_template("topic_update.html", post = post)

@app.route("/topic/show/<int:id>")
def topic_show(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)

    return render_template("topic_show.html", post = post)

@app.route("/topic/delete/<int:id>")
def topic_delete(id):
    try:
        post_store.delete(id)
    except ValueError:
        abort(404)

    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
