from app import models, db
from sqlalchemy import desc, func


class BaseStore():

    def __init__(self, data_provider):
        self.data_provider = data_provider

    def get_all(self):
        return self.data_provider.query.all()

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def get_by_id(self, id):
        return self.data_provider.query.get(id)

    def update(self, entity, fields):
        result = self.data_provider.query.filter_by(id = entity.id).update(fields)
        db.session.commit()
        return result

    def delete(self, id):
        result = self.data_provider.query.filter_by(id = id).delete()
        db.session.commit()
        return result

    def entity_exists(self, entity):
        result = True

        if self.get_by_id(entity.id) is None:
            result = False

        return result


class MemberStore(BaseStore):

    def __init__(self):
        super().__init__(models.Member)

    def get_by_name(self, member_name):
        return self.data_provider.query.filter_by(name = member_name)

    def update(self, entity):
        fields = {"name": entity.name, "age": entity.age}
        return super().update(entity, fields)

    def get_members_with_posts(self):
        return self.data_provider.query.join(models.Member.posts)

    def get_top_two(self):
        return self.data_provider.query(func.count(models.Member.posts).label('total')).order_by('total DESC')


class PostStore(BaseStore):

    def __init__(self):
        super().__init__(models.Post)

    def update(self, entity):
        fields = {"title": entity.title, "content": entity.content}
        return super().update(entity, fields)
