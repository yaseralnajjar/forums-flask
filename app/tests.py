from app import models, stores, dummy_data

def create_members():
    member1 = models.Member("Mohammed", 20)
    member2 = models.Member("Mohammed", 22)
    member3 = models.Member("Abdo", 25)
    print(member1)
    print(member2)
    print(member3)
    print("=" * 30)

    return member1, member2, member3


def store_should_add_members(members_instances, member_store):
    for member in members_instances:
        member_store.add(member)


def stores_should_be_similar():
    member_store1 = stores.MemberStore()
    member_store2 = stores.MemberStore()
    if member_store1.get_all() is member_store2.get_all():
        print("Same stores elements !")


def print_members_list(members_list):
    for member in members_list:
        print(member)


def print_all_members(member_store):
    print("=" * 30)

    print_members_list(member_store.get_all())

    print("=" * 30)


def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(2)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")


def update_should_modify_object(member_store, member3):
    member3_copy = models.Member.query.get(3)

    print(member3_copy)
    member3_copy.name = "John"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))


def store_should_get_members_by_name(member_store):

    print("*" * 30)
    print("Getting by name:")
    members_by_name_retrieved = member_store.get_by_name("Mohammed")
    print_members_list(members_by_name_retrieved)


def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")


def create_posts(members_instances):

    post1 = models.Post("Agriculture", "Agriculture is amazing", members_instances[0].id)
    post2 = models.Post("Engineering", "I love engineering", members_instances[0].id)

    post3 = models.Post("Medicine", "Medicine is great", members_instances[1].id)
    post4 = models.Post("Architecture", "Spectacular art", members_instances[1].id)
    post5 = models.Post("Astronomy", "Space is awesome", members_instances[1].id)

    post6 = models.Post("Geology", "Earth is our friend", members_instances[2].id)
    post7 = models.Post("ComputerSci", "Our passion", members_instances[2].id)
    post8 = models.Post("Algorithms", "Yeah, more of that", members_instances[2].id)
    post9 = models.Post("Operating Systems", "Ewww", members_instances[2].id)

    print(post1)
    print(post2)
    print(post3)
    print("=" * 30)

    return post1, post2, post3, post4, post5, post6, post7, post8, post9


def store_should_add_posts(posts_instances, post_store):
    for member in posts_instances:
        post_store.add(member)


def store_should_get_members_with_posts(member_store):
    members_with_posts = member_store.get_members_with_posts()

    for member_with_posts in members_with_posts:
        print(f"{member_with_posts} has posts:")
        for post in member_with_posts.posts:
            print(f"\t{post}")

        print("=" * 10)


def store_should_get_top_two(member_store):
    top_two_members = member_store.get_top_two()

    for member_with_posts in top_two_members:
        print(f"{member_with_posts} has posts:")
        for post in member_with_posts.posts:
            print(f"\t{post}")


member_store = stores.MemberStore()
post_store = stores.PostStore()

members_instances = dummy_data.dummy_members
member1, member2, member3 = members_instances

posts_instances = dummy_data.dummy_posts
post1, post2, post3, post4, post5, post6, post7, post8, post9 = posts_instances

store_should_add_members(members_instances, member_store)

stores_should_be_similar()

print_all_members(member_store)

get_by_id_should_retrieve_same_object(member_store, member2)

update_should_modify_object(member_store, member3)

catch_exception_when_deleting()

print_all_members(member_store)

store_should_get_members_by_name(member_store)

store_should_add_posts(posts_instances, post_store)

store_should_get_members_with_posts(member_store)

#store_should_get_top_two(member_store)

