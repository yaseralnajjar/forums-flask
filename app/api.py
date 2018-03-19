from flask import request, jsonify, abort
from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.as_dict() for post in post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/show/<int:id>")
def topic_show_api(id):
    post = post_store.get_by_id(id)
    try:
        result = jsonify(post.as_dict())
    except AttributeError:
        result = abort(404, f"topic with id: {id} doesn't exist")

    return result


@app.route("/api/topic/delete/<int:id>", methods = ["DELETE"])
def topic_delete_api(id):
    try:
        post_store.delete(id)
        result = jsonify({"message": "Deleted item successfully !"})
    except ValueError:
        result = abort(404, f"topic with id: {id} doesn't exist")

    return result


@app.route("/api/topic/add", methods = ["POST"])
def topic_add_api():
    request_data = request.get_json()
    try:
        new_post = models.Post(title = request_data["title"], content = request_data["content"])
        post_store.add(new_post)
        result = jsonify(new_post.as_dict())
    except KeyError:
        result = abort(400, f"Couldn't parse the request data !")

    return result


@app.route("/api/topic/update/<int:id>", methods = ["PUT"])
def topic_update_api(id):
    request_data = request.get_json()
    post = post_store.get_by_id(id)
    try:
        post.title = request_data["title"]
        post.content = request_data["content"]
        post_store.update(post)
        result = jsonify(post.as_dict())
    except AttributeError:
        result = abort(404, f"topic with id: {id} doesn't exist")
    except KeyError:
        result = abort(400, f"Couldn't parse the request data !")

    return result


@app.errorhandler(400)
def bad_request(error):
    return jsonify(message = error.description)
