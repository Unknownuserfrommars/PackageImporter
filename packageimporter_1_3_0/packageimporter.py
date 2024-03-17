# Welcome to Version 1.3.0 of PackageImporter, released March 17, 2024 (Timezone unreliable)

import importlib as impl
import pip
import subprocess as spc
import sys

cv = '1.3.0'

class PackageImporterVersionCheck:
    def Out():
        print(f'Current Version: {cv}')
    def Ret():
        f = f'Current Version: {cv}'
        return f

class Pip:
    class Installed:
        class Pkg:
            def get_pkg_list():
                try:
                    return pip.main(["List"])
                except Exception as e:
                    print(f"An exception '{e}' occured, using subprocess to get list")
                    spc.run(["pip", "list"])
    class InstallPkg:
        def installpackage(package_name):
            spc.check_call(sys.executable, "-m", "pip", "install", package_name)


class Importer:
    class MyOwnModules:
        modules = {
            'pyprogramsimp': 'pprogs',
            'graphgame': 'gg',
            'packageimporter': 'pimport',
        }

        @staticmethod
        def import_module(module_name, alias=None):
            """Import a single module with optional alias, error is raised if package is not globally installed"""
            try:
                if alias:
                    globals()[alias] = impl.import_module(module_name)
                else:
                    globals()[module_name.split('.')[-1]] = impl.import_module(module_name)
            except ModuleNotFoundError:
                raise ModuleNotFoundError(
                    f"The module '{module_name}'is not globally installed, please install it first using pip, or install it using Pip.InstallPkg.installpackage({module_name})"
                )

        @classmethod
        def all(cls):
            for module_name, pip_name in cls.modules.items():
                cls.import_module(module_name, pip_name if pip_name else module_name)

        @classmethod
        def pyprogramsimp(cls, alias):
            cls.import_module('pyprogramsimp', alias)

        @classmethod
        def graphgame(cls, alias):
            cls.import_module('graphgame', alias)

        @classmethod
        def packageimporter(cls, alias):
            cls.import_module('packageimporter', alias)
    class ScienceAndMaths:
        modules = {
            'scipy': None,
            'sympy': None,
        }
        
        @staticmethod
        def import_module(module_name, alias=None):
            """Import a single module with optional alias, error is raised if package is not globally installed"""
            try:
                if alias:
                    globals()[alias] = impl.import_module(module_name)
                else:
                    globals()[module_name.split('.')[-1]] = impl.import_module(module_name)
            except ModuleNotFoundError:
                raise ModuleNotFoundError(
                    f"The module '{module_name}'is not globally installed, please install it first using pip, or install it using Pip.InstallPkg.installpackage({module_name})"
                )

        @classmethod
        def scipy(cls, alias=None):
            cls.import_module('scipy', alias)

        @classmethod
        def sympy(cls, alias=None):
            cls.import_module('sympy', alias)

        @classmethod
        def all(cls):
            for module_name, pip_name in cls.modules.items():
                cls.import_module(module_name, pip_name if pip_name else module_name)
    class DataScience:
        modules = {
        'pandas': None,
        'numpy': None,
        'sklearn': 'scikit-learn',
        }

        @staticmethod
        def import_module(module_name, alias=None):
            """Import a single module with optional alias, error is raised if package is not globally installed"""
            try:
                if alias:
                    globals()[alias] = impl.import_module(module_name)
                else:
                    globals()[module_name.split('.')[-1]] = impl.import_module(module_name)
            except ModuleNotFoundError:
                raise ModuleNotFoundError(
                    f"The module '{module_name}'is not globally installed, please install it first using pip, or install it using Pip.InstallPkg.installpackage({module_name})"
                )
        
        @classmethod
        def pandas(cls, alias=None):
            cls.import_module('pandas', alias)

        @classmethod
        def numpy(cls, alias=None):
            cls.import_module('numpy', alias)

        @classmethod
        def sklearn(cls, alias): # default alias is sklearn
            cls.import_module('sklearn', alias)

        @classmethod
        def all(cls):
            for module_name, pip_name in cls.modules.items():
                cls.import_module(module_name, pip_name if pip_name else module_name)
    
    class Plotter:
        class matplotlib:
            modules = {
                'matplotlib.pyplot': 'plt',
                'matplotlib.style': 'style',
            }

            @staticmethod
            def import_module(module_name, alias):
                """Import a single module with an alias"""
                try:
                    module = impl.import_module(module_name)
                    if alias:
                        globals()[alias] = module
                    else:
                        default_alias = Importer.stable.Plotter.modules.get(module_name, module_name.split('.')[-1])
                        globals()[default_alias] = module
                except ModuleNotFoundError:
                    raise ModuleNotFoundError(
                        f"The module '{module_name}'is not globally installed, please install it first using pip, or install it using Pip.InstallPkg.installpackage({module_name})"
                    )
            
            @classmethod
            def all(cls):
                for alias, module_name in cls.modules.items():
                    cls.import_module(module_name, alias)

            @classmethod
            def pyplot(cls, alias=None): # default alias is plt
                cls.import_module('matplotlib.pyplot', alias)
                
            @classmethod
            def style(cls, alias=None):
                cls.import_module('matplotlib.style', alias)
            
        class plotly:
            modules = {
                'plotly.express': 'px',
                'plotly.graph_objects': 'go',
                'plotly.subplots': 'make_subplots',
            }

            @staticmethod
            def import_module(module_name, alias=None):
                """Import a single module with an optional alias."""
                try:
                    module = impl.import_module(module_name)
                    if alias:
                        globals()[alias] = module
                    else:
                        # Use the default alias or module name if no alias is provided
                        default_alias = Importer.stable.Plotter.modules.get(module_name, module_name.split('.')[-1])
                        globals()[default_alias] = module
                except ModuleNotFoundError:
                    raise ModuleNotFoundError(
                        f"The module '{module_name}'is not globally installed, please install it first using pip, or install it using Pip.InstallPkg.installpackage({module_name})"
                    )
                
            @classmethod
            def express(cls, alias=None):
                cls.import_module('plotly.express', alias)
                
            @classmethod
            def graph_objects(cls, alias=None):
                cls.import_module('plotly.graph_objects', alias)
                
            @classmethod
            def subplots(cls, alias=None):
                cls.import_module('plotly.subplots', alias)

            @classmethod
            def all(cls):
                for alias, module_name in cls.modules.items():
                    cls.import_module(module_name, alias)
    class Builtins:
        modules = {
            'random': None,
            'time': None,
            'sys': None,
            'os': None,
        }
        def import_module(module_name, alias=None):
            try:
                module = impl.import_module(module_name)
                if alias:
                    globals()[alias] = module
                else:
                    default_alias = Importer.stable.Builtins.modules.get(module_name, module_name.split('.')[-1])
                    globals()[default_alias] = module
            except ModuleNotFoundError as e:
                raise e(f"The module '{module_name}'is not globally installed, please install it first using pip, or install it using Pip.InstallPkg.installpackage({module_name})")
            
        @classmethod
        def all(cls):
            for alias, module_name in cls.modules.items():
                cls.import_module(module_name, alias)

        @classmethod
        def random(cls, alias=None):
            cls.import_module("random", alias)

        @classmethod
        def time(cls, alias=None):
            cls.import_module("time", alias)
        
        @classmethod
        def sys(cls, alias=None):
            cls.import_module("sys", alias)
        
        @classmethod
        def os(cls, alias=None):
            cls.import_module("os", alias)