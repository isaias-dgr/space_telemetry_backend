
import vizro.models as vm
import vizro.plotly.express as px

from app.adapters.https.vizro.services.space_service import SpaceService

def get_satellites():
    data = SpaceService()
    iris_data = px.data.iris()
    return vm.Page(
    title="Second Page",
    components=[
        vm.Graph(
            id="scatter_iris",
            figure=px.scatter(iris_data, x="sepal_width", y="sepal_length", color="species",
                color_discrete_map={"setosa": "#00b4ff", "versicolor": "#ff9222"},
                labels={"sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
                        "species": "Species"},
            ),
        ),
        vm.Graph(
            id="hist_iris",
            figure=px.histogram(iris_data, x="sepal_width", color="species",
                color_discrete_map={"setosa": "#00b4ff", "versicolor": "#ff9222"},
                labels={"sepal_width": "Sepal Width", "count": "Count",
                        "species": "Species"},
            ),
        ),
    ],
    controls=[
        vm.Parameter(
            targets=["scatter_iris.color_discrete_map.virginica",
                        "hist_iris.color_discrete_map.virginica"],
            selector=vm.Dropdown(
                options=["#ff5267", "#3949ab"], multi=False, value="#3949ab", title="Color Virginica"),
            ),
        vm.Parameter(
            targets=["scatter_iris.opacity"],
            selector=vm.Slider(min=0, max=1, value=0.8, title="Opacity"),
        ),
    ],
)