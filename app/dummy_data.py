from app import models

dummy_members = [
    models.Member("Mohammed", 20),
    models.Member("Mohammed", 22),
    models.Member("Abdo", 25),
]

dummy_posts = [
    models.Post("Agriculture", "Agriculture is amazing", dummy_members[0].id),
    models.Post("Engineering", "I love engineering", dummy_members[0].id),

    models.Post("Medicine", "Medicine is great", dummy_members[1].id),
    models.Post("Architecture", "Spectacular art", dummy_members[1].id),
    models.Post("Astronomy", "Space is awesome", dummy_members[1].id),

    models.Post("Geology", "Earth is our friend", dummy_members[2].id),
    models.Post("ComputerSci", "Our passion", dummy_members[2].id),
    models.Post("Algorithms", "Yeah, more of that", dummy_members[2].id),
    models.Post("Operating Systems", "Ewww", dummy_members[2].id),
]

def seed_stores(member_store, post_store):
    for member in dummy_members:
        member_store.add(member)

    for post in dummy_posts:
        post_store.add(post)
