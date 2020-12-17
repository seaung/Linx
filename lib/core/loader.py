import importlib.abc
import importlib.util

from lib.tools.utils import get_md5


class LoaderPlugins(importlib.abc.Loader):
    def __init__(self, fullname, path):
        self.fullname = fullname
        self.path = path
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_filename(self):
        return self.path

    def get_data(self, filename):
        if filename.startswith("Linx://") and self.data:
            data = self.data
        else:
            with open(filename, encoding="utf-8") as fs:
                data = fs.read()
        return data

    def exec_plugin(self, plugin):
        filename = self.get_filename(self.fullname)
        plugin_code = self.get_data(filename)
        obj = compile(plugin_code, filename, "exec", dont_inherit=True, optimize=-1)
        exec(obj, plugin.__dict__)


def loader_string_to_plugin(code_string, fullname=None):
    try:
        plugin_name = "plugins_{0}".format(get_md5(code_string)) if fullname is None else fullname
        file_path = "Linx://{0}".format(plugin_name)
        plugin_loader = LoaderPlugins(plugin_name, file_path)
        plugin_loader.set_data(code_string)
        spec = importlib.util.spec_from_file_location(plugin_name, file_path, loader=plugin_loader)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_plugin(plugin)
        return plugin
    except ImportError:
        error_msg = "loader plugin failed : {0}".format(fullname)
        raise
