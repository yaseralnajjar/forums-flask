from app import models, db

dummy_members = [
    models.Member(name="Mohammed", age=20),
    models.Member(name="Mohammed", age=22),
    models.Member(name="Abdo", age=25),
]

dummy_posts = [
    models.Post(title="Agriculture", content="Agriculture is amazing", member_id=1),
    models.Post(title="Engineering", content="I love engineering", member_id=1),

    models.Post(title="Medicine", content="Medicine is great", member_id=2),
    models.Post(title="Architecture", content="Spectacular art", member_id=2),
    models.Post(title="Astronomy", content="Space is awesome", member_id=2),

    models.Post(title="Geology", content="Earth is our friend", member_id=3),
    models.Post(title="ComputerSci", content="Our passion", member_id=3),
    models.Post(title="Algorithms", content="Yeah, more of that", member_id=3),
    models.Post(title="Operating Systems", content="Ewww", member_id=3),
]


def seed_stores(member_store, post_store):
    db.drop_all()
    db.create_all()

    for member in dummy_members:
        member_store.add(member)

    for post in dummy_posts:
        post_store.add(post)
