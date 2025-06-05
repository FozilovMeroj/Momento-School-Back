import i18n

import app.config as config


def init_i18n() -> None:
    i18n.load_path.append("lang")
    i18n.set("locale", config.LOCALE)
    i18n.set("skip_locale_root_data", True)
