import importlib
import pkgutil


def load_routers(app, path, base_module="app.api", prefix=""):
    for finder, name, ispkg in pkgutil.iter_modules([str(path)]):
        module_name = f"{base_module}.{name}"
        full_path = path / name

        if ispkg:
            load_routers(app, full_path, module_name, prefix + f"/{name}")
        else:
            module = importlib.import_module(module_name)
            if hasattr(module, "router"):
                router = getattr(module, "router")
                print(router)
                app.include_router(router, prefix=prefix + f"/{name.split('.')[0]}")
                print(f"Mounted {module_name} at {prefix}/{name.split('.')[0]}")
