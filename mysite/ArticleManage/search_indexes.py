from haystack import indexes
from .models import ArticlePost

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created = indexes.DateTimeField(model_attr="created")

    def get_model(self):
        return ArticlePost

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
