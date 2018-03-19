import copy
import itertools


class BaseStore():

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        all_instances = self.get_all()

        result = None

        for item in all_instances:
            if item.id == id:
                result = item
                break

        return result

    def update(self, instance):
        result = instance
        all_instances = self.get_all()

        # This is not pythonic !
        # Just for demonstration
        # If you wanna know the pythonic code, use comprehension:
        # https://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python
        for index, current_instance in enumerate(all_instances):
            if current_instance.id == instance.id:
                all_instances[index] = instance
                break

        return result

    def delete(self, id):
        instance = self.get_by_id(id)
        self._data_provider.remove(instance)

        return instance

    def entity_exists(self, instance):
        result = True

        if self.get_by_id(instance.id) is None:
            result = False

        return result


class MemberStore(BaseStore):

    members = []
    last_id = 1

    def __init__(self):
        super().__init__(MemberStore.members, MemberStore.last_id)

    def get_by_name(self, member_name):
        all_members = self.get_all()

        for member in all_members:
            if member.name == member_name:
                yield member

    def get_members_with_posts(self, all_posts):
        all_members = copy.deepcopy(self.get_all())

        #def append_post(member, post):
        #    member.posts.append(post)
        #    return member

        #result = [(append_post(member, post))
        #          for member in all_members
        #          for post in all_posts
        #          if member.id == post.member_id]

        #result = ((append_post(member, post))
        #          for member, post
        #          in itertools.product(all_members, all_posts)
        #          if member.id == post.member_id)

        for member, post in itertools.product(all_members, all_posts):
            if member.id == post.member_id:
                member.posts.append(post)

        for member in all_members:
            yield member


    #def load_posts(self, member, all_posts):
    #    for post in all_posts:
    #        if post.member_id == member.id:
    #            member.posts.append(post)
    #
    #    return member

    def get_top_two(self, all_posts):
        members_with_posts = list(self.get_members_with_posts(all_posts))

        members_with_posts.sort(key=lambda member: len(member.posts), reverse=True)

        yield members_with_posts[0]
        yield members_with_posts[1]
        #for member in members_with_posts:
        #    if len(member.posts) >= 10:
        #        yield member


class PostStore(BaseStore):

    posts = []
    last_id = 1

    def __init__(self):
        super().__init__(PostStore.posts, PostStore.last_id)

    #def get_all(self):
    #    return PostStore.posts
#
    #def add(self, post):
    #    post.id = PostStore.last_id
    #    PostStore.posts.append(post)
    #    PostStore.last_id += 1
#
    #def get_by_id(self, id):
    #    all_posts = self.get_all()
#
    #    result = None
#
    #    for post in all_posts:
    #        if post.id == id:
    #            result = post
    #            break
#
    #    return result
#
    #def update(self, post):
    #    result = post
    #    all_posts = self.get_all()
#
    #    for index, current_post in enumerate(all_posts):
    #        if current_post.id == post.id:
    #            all_posts[index] = post
    #            break
#
    #    return result
#
    #def delete(self, id):
    #    post = self.get_by_id(id)
    #    PostStore.posts.remove(post)
#
    #def entity_exists(self, post):
    #    result = True
#
    #    if self.get_by_id(post.id) is None:
    #        result = False
#
    #    return result
