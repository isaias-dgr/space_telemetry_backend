import vizro.models as vm
from vizro import Vizro

from app.adapters.https.vizro.components.pages.home import get_home_page
from app.adapters.https.vizro.components.pages.launchers import get_launches
from app.adapters.https.vizro.components.pages.satellites import get_satellites

home_page = get_home_page()
launches_page = get_launches()
satellites_page = get_satellites()

dashboard = vm.Dashboard(pages=[home_page, launches_page, satellites_page])

app = Vizro().build(dashboard)

if __name__ == "__main__":
    app.run()