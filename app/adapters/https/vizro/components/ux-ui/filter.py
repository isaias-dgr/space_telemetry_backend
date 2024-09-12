
import vizro.plotly.express as px

df = px.data.gapminder()
gapminder_data = (
        df.groupby(by=["continent", "year"]).
            agg({"lifeExp": "mean", "pop": "sum", "gdpPercap": "mean"}).reset_index()
    )