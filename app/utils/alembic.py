import importlib
import pathlib


def import_all_models(package_name: str, package_path: str):
    """
    Recursively import all Python modules in a given package.
    """
    print(package_path)
    for path in pathlib.Path(package_path).rglob("*.py"):
        if path.name == "__init__.py":
            continue
        module_path = path.with_suffix("").relative_to(package_path)
        module_str = ".".join((package_name,) + module_path.parts)
        print(module_str)
        importlib.import_module(module_str)
