from ui.events.event_handler import EventHandler
from kubernetes.kubernetes_api_factory import KubernetesApiFactory


class ContextEventHandler(EventHandler):
    def proces_event(self, event):
        new_context_id = self.caller.context_selector.value[0]
        new_context = self.caller.all_contexts[new_context_id]


        self.caller.update_status_box("Thinking about changing context Master?")

        if self.caller.current_context != new_context:
            self.caller.current_context = new_context

            self.caller.update_status_box("Setting new context in Kubernetes: "
                                          + new_context)

            self.kubernetes_api = (KubernetesApiFactory(context=new_context)
                                   .build_kubernetes_api())
            self.caller.parentApp.update_kubernetes_api(self.kubernetes_api)
            self.caller.update_status_box("Retrieving clusters within context")
            all_clusters = self.kubernetes_api.all_clusters
            current_cluster, current_cluster_id = (
                 self.kubernetes_api.current_cluster)

            self.caller.update_status_box("Changing clusters within form")
            self.caller.update_cluster_selector(all_clusters,
                                                current_cluster,
                                                current_cluster_id)

            self.caller.update_status_box("Context confirmed! Ready my master")
