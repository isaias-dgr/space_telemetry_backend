from vizro import Vizro
import vizro.models as vm

from app.adapters.https.vizro.services.space_service import SpaceService


def get_home_page():
    data = SpaceService()
    
    return vm.Page(
    title="Homepage",
    components=[
        vm.Card(
            text="""
            ![](https://raw.githubusercontent.com/mckinsey/vizro/786167c822cce65fe85ffad8ed000d8553a5ef44/vizro-core/docs/assets/images/collections.svg)

            ### Rockets and Launches

            SpaceX, the aerospace company founded by Elon Musk, has revolutionized the rocket and space launch industry. Its reusable rockets, such as the Falcon 9 and Falcon Heavy, have significantly reduced the cost of space access, enabling more frequent and efficient launches. SpaceX has successfully completed numerous missions, both commercial and governmental, sending satellites into Earth’s orbit, delivering supplies to the International Space Station, and paving the way for future crewed missions to Mars. Their focus on rocket reusability has changed the game in space exploration.
            """,
            href="/rockets-launches",
        ),
        vm.Card(
            text="""
            ![](https://raw.githubusercontent.com/mckinsey/vizro/786167c822cce65fe85ffad8ed000d8553a5ef44/vizro-core/docs/assets/images/features.svg#icon-top)

            ### Satellites

            Starlink is a satellite internet constellation developed by SpaceX with the aim of providing high-speed, low-latency broadband internet across the globe, particularly in remote and underserved areas. Comprising thousands of small, low Earth orbit (LEO) satellites, Starlink is designed to offer a reliable alternative to traditional ground-based internet infrastructure. The satellites communicate with each other via laser links and are deployed in a network that allows for continuous coverage as they orbit the Earth. By drastically reducing the cost of satellite launches with reusable rockets like the Falcon 9, SpaceX has rapidly expanded the Starlink constellation, making affordable global internet access a reality for many.
            """,
            href="/second-page",
        ),
    ],
)