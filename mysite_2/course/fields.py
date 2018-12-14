from django.db import models
from django.core.exceptions import ObjectDoesNotExist
class OrderField(models.PositiveIntegerField): #③
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super(OrderField, self).__init__(*args, **kwargs)
    def pre_save(self, model_instance, add): #④
        if getattr(model_instance, self.attname) is None: #⑤
            try:
                qs = self.model.objects.all() #⑥
                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields} #⑦
                    qs = qs.filter(**query) #⑧
                last_item = qs.latest(self.attname) #⑨
                value = last_item.order + 1 #⑩
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value) #⑪
            return value
        else:
            return super(OrderField, self).pre_save(model_instance, add)