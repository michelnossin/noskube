from ui.events.event_handler import EventHandler
from kubernetes.kubernetes_api_factory import KubernetesApiFactory


class ContextEventHandler(EventHandler):
    def proces_event(self, event):
        app = self.caller.parentApp
        kubernetes = app.kubernetes_api

        new_context_id = self.caller.context_selector.value[0]
        new_context = (kubernetes.all_contexts[new_context_id])

        self.caller.update_status_box("Changing context Master?")

        if app.current_context != new_context:
            app.current_context = new_context

            self.caller.update_status_box("Setting new context in Kubernetes: "
                                          + new_context)

            new_api = (
                 KubernetesApiFactory(context=new_context)
                 .build_kubernetes_api())
            app.update_kubernetes_api(new_api)
            self.caller.update_status_box("Retrieving clusters within context")
            current_cluster, current_cluster_id = (kubernetes.current_cluster)

            self.caller.update_status_box("Changing clusters within form")
            self.caller.update_cluster_selector(kubernetes
                                                .all_clusters,
                                                current_cluster,
                                                current_cluster_id)
            self.caller.update_namespace_selector(kubernetes
                                                  .all_namespaces,
                                                  self.caller
                                                  .namespace_selector.value[0],
                                                  app.current_namespace_id)

            self.caller.update_status_box("Context confirmed! Ready my master")
