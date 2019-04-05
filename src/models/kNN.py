from .base import BaseModel
import sklearn.neighbors.classification as knn


class KNNModel(BaseModel):
    def __init__(self, author=None, name=None, **kwargs):
        super().__init__(author=author, name=name, **kwargs)

        self.model = knn.KNeighborsClassifier()

    def _model_train(self, data, **kwargs):
        x, y = self.get_data(data)
        self.model.fit(x, y)

    def _estimate(self, x, y, **kwargs):
        result = self.model.predict(x)
        score = self.model.score(x, y)
        return result.tolist(), score