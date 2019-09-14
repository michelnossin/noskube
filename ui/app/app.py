import npyscreen

from ui.forms.main_form import MainForm
from ui.forms.pod_form import PodForm

import constants as c


class App(npyscreen.StandardApp):
    def __init__(self, kubernetes_api):
        super().__init__()
        self.kubernetes_api = kubernetes_api
        self.current_context, self.current_context_id = (self
                                                         .kubernetes_api
                                                         .current_context)
        self.current_cluster, self.current_cluster_id = (self
                                                         .kubernetes_api
                                                         .current_cluster)
        self.current_namespace_id = 0

    def update_kubernetes_api(self, kubernetes_api):
        self.kubernetes_api = kubernetes_api

    def onStart(self):
        self.addForm("POD", PodForm, name="NosKube Professional Edition",
                     lines=c.Y_ROWS_FULL)
        self.addForm("MAIN", MainForm, name="NosKube Professional Edition",
                     lines=c.Y_ROWS_FULL)
