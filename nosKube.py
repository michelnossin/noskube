from kubernetes.kubernetes_api_factory import KubernetesApiFactory
from ui.app.app import App

if __name__ == "__main__":
    kubernetes_api = KubernetesApiFactory().build_kubernetes_api()
    MyApp = App(kubernetes_api)
    MyApp.run()
