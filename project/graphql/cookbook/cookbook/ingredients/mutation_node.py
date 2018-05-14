# coding:utf8
import graphene


class Episode(graphene.Enum):
    """参考python中的enum用法"""
    NEWHOPE = 4
    EMPIRE = 5
    JEDI = 6

    @property
    def description(self):
        if self == Episode.NEWHOPE:
            return 'New Hope Episode'
        elif self == Episode.EMPIRE:
            return 'New EMPIRE Episode'
        elif self == Episode.JEDI:
            return 'New JEDI Episode'
        else:
            return 'Other episode'


