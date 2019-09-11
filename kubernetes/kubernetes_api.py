from pykube.config import KubeConfig


class KubernetesApi(KubeConfig):
    def __init__(self, config_file_name='~/.kube/config', context=None):
        self.config = KubeConfig.from_file(config_file_name,
                                           current_context=context)

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
