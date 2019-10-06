from .modules.Core import Core


class UfrnApi(Core):
    """Classe que reune todos os módulos do pacote.
    """
    def __init__(self, client_id: str, client_secret: str,
                 x_api_key: str, version: str):
        """Construtor do pacote. Passa atributos pra classe Env.
        """
        super().__init__(client_id, client_secret, x_api_key, version)

    def print_resources(self) -> None:
        """Imprime na tela os recursos presentes na API.
        """
        for resource in self._request_get(self.url_base + 'documentacao'):
            print(
                "Nome: {},\nUrl: {},\n".format(
                    resource['name'],
                    self._format_url_to_resource(resource['url']),
                )
            )

    def print_resources_details(self, name) -> None:
        """ Imprime na tela as categorias de dados
        presentes no recurso da API escolhido pelo usuário
        """
        url = ''
        for resource in self._request_get(self.url_base + 'documentacao'):
            if resource['name'] == name:
                url = self._format_url_to_resource(resource['url'])
                break

        for sub_resource in self._request_get(url)['tags']:
            print(
                "Nome: {}\nDescription: {}\n".format(
                    sub_resource['name'],
                    sub_resource['description']
                )
            )
