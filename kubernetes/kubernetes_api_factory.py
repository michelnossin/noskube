from kubernetes.kubernetes_api import KubernetesApi


class KubernetesApiFactory():
    def __init__(self, config_file_name='~/.kube/config', context=None):
        self.config_file_name = config_file_name
        self.context = context

    def build_kubernetes_api(self):
        return KubernetesApi(self.config_file_name,
                             self.context)
