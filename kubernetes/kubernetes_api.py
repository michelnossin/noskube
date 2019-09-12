from pykube.config import KubeConfig
from pykube.objects import Pod, Deployment, Namespace

from pykube import HTTPClient


class KubernetesApi(KubeConfig):
    def __init__(self, config_file_name='~/.kube/config', context=None):
        self.config = KubeConfig.from_file(config_file_name,
                                           current_context=context)
        self.kubernetes_api = HTTPClient(self.config)

    @property
    def api_server(self):
        return self.kubernetes_api

    @property
    def current_context(self):
        return (self.config.current_context,
                self.all_contexts.index(self.config.current_context))

    @property
    def all_contexts(self):
        return [x for x in self.config.contexts.keys()]

    @property
    def current_cluster(self):
        return (self.config.cluster["server"],
                self.all_clusters.index(self.config.cluster["server"]))

    @property
    def all_clusters(self):
        return [y
                for x, y
                in self.config.clusters[self.current_context[0]].items()
                if x == "server"]

    @property
    def all_pods(self):
        try:
            return [pod
                    for pod
                    in Pod.objects(self.api_server)]
        finally:
            return ["It seems this cluster is not up and running?"]

    @property
    def all_deployments(self):
        try:
            return [deployment
                    for deployment
                    in Deployment.objects(self.api_server)]
        except:
            return ["It seems this cluster is not up and running?"]

    @property
    def all_namespaces(self):
        try:
            return ["all"] + [str(ns)
                              for ns
                              in Namespace.objects(self.api_server)]
        except:
            return ["It seems this cluster is not up and running?"]
