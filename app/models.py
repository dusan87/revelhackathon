from database import db

class RevelResource(db.Model):
    """
    It represents simple model where sent data from Revel will be stored.
    Also, it gives an idea how to process retrieved data,
    make rich content either to own app or push to third-party application.
    """

    id = db.Column(db.Integer, primary_key=True)
    revel_id = db.Column(db.Integer, doc='ID of resource on in Revel system')
    updated = db.Column(db.Boolean, default=False, doc='Helper for filtering while displaying')
    name = db.Column(db.String, doc='Helper for keeping Revel resource name for filtering while displaying')

    created_date = db.Column(db.String, doc='Expose an idea how to manipulate received data')
    updated_date = db.Column(db.String, default='---', doc='Expose an idea how to manipulate received data')
    data = db.Column(db.String, doc=("Content of created/updated resource." 
                                     "Format of content is JSON string"))

    def __repr__(self,):
        return "<RevelResource (%r, %r)>" % (self.resource_name, self.id)

    @classmethod
    def get_all(cls,):
        """
        This is like a model manager to query all().
        """
        return cls.query.all()

    @property
    def name_plural(self,):
        return "{}s".format(self.name)