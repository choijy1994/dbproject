import pymysql
from django.db.models import Q

class restaurant():
        def recommend(kind=None, cost=None, dist=None, rate=None):
                q = Q()
                if kind != None:
                        q &= Q(kind=kind)
                if cost != None:
                        if cost == '$':
                                q &= Q(cost='$')
                        elif cost == '$$':
                                q &= (Q(cost='$') | Q(cost='$$'))
                if dist != None:
                        q &= Q(dist__lte=int(dist))
                if rate != None:
                        q &= Q(rate__gte=float(rate))
                return q
