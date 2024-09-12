import pandas as pd
import vizro.models as vm
import vizro.plotly.express as px

from app.adapters.https.vizro.services.space_service import SpaceData, SpaceService


def get_launches():
    data = SpaceService()
    return vm.Page(
    title="Rockets & Launches",
    path="/rockets-launches",
    layout=vm.Layout(grid=[[0, 0, 0, 1, 2],
                           [3, 4, 5, 6, 7],
                           [8, 8, 9, 9, 10],
                           [8, 8, 9, 9, 10],
                           [11, 11, 11, 11, 11]]),
    components=[
        vm.Card(text="""SpaceX, the aerospace company founded by Elon Musk, has revolutionized the rocket and space launch industry. Its reusable rockets, such as the Falcon 9 and Falcon Heavy, have significantly reduced the cost of space access, enabling more frequent and efficient launches. SpaceX has successfully completed numerous missions, both commercial and governmental, sending satellites into Earth’s orbit, delivering supplies to the International Space Station, and paving the way for future crewed missions to Mars. Their focus on rocket reusability has changed the game in space exploration."""),

        getPie("Launch Success Rate", *data.get_label_values(SpaceData.LAUNCH_SUCCESS_RATE)),
        getPie("Reusability Count", *data.get_label_values(SpaceData.REUSABILITY_COUNT)),
        
        getCard("Average Thrust", data.get_data(SpaceData.AVERAGE_THRUST), "Average thrust of rockets"),
        getCard("Cost per Launch", data.get_data(SpaceData.COST_PER_LAUNCH_AVG), "Average cost per launch"),
        getCard("Engine Count", data.get_data(SpaceData.ENGINE_COUNT_AVG), "Average engine count"),
        getCard("Payload Weight", data.get_data(SpaceData.PAYLOAD_WEIGHT_AVG), "Average payload weight"),
        getCard("Stage Burn Time", data.get_data(SpaceData.STAGE_BURN_TIME_AVG), "Average stage burn time"),
        getPie("Distribution of clients", *data.get_label_values(SpaceData.CLIENT_DISTRIBUTION)),

        getPie("Launch Orbits", *data.get_label_values(SpaceData.LAUNCH_ORBITS)),
        getPie("Cost Comparison by Rocket Type", *data.get_label_values(SpaceData.COST_COMPARISON_BY_ROCKET_TYPE)),
        getLine("Launches per Year", *data.get_histogram_values(SpaceData.LAUNCHES_PER_YEAR)),
        ],
    )



def getCard(title, value, description):
    return vm.Card(
        text=f"""
            ## {title}
            # {value}
            ### {description}
        """,
        href="/rockets-launches",
    )

def getPie(title, values, labels):
    df = pd.DataFrame({"values": values, "labels": labels})
    return vm.Graph(
        id=title,
        figure=px.pie(df, values='values', names='labels', title=title),
    )


def getLine(title, values, labels):
    df = pd.DataFrame({"values": values, "labels": labels})
    return vm.Graph(
        id=title,
        figure=px.line(df, x='values', y='labels', title=title),
    )