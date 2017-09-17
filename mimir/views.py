from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.jinja2')
def home(request):
    return {'project': 'Mimir'}


@view_config(route_name='cipher', renderer='templates/cipher.jinja2')
def cipher(request):
    return {}


@view_config(route_name='encoding', renderer='templates/encoding.jinja2')
def encoding(request):
    import addons.encoding as enc
    encoding_algos = {
        "all": "all"
    }

    for a in enc.get_algorithms():
        encoding_algos[a.name] = a

    a = 5

    # TODO allow files as well
    return {
        "encodings": encoding_algos
    }


class ToolViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='tools', renderer='templates/tools/tools.jinja2')
    def tools(self):
        return {}

    @view_config(route_name='tools/rest', renderer='templates/tools/rest.jinja2')
    def rest(self):
        return {}
