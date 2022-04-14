class TestData:
    BASE_URL = "https://www.apple.com/"

    LANG_CODES = {
        "Turkey": "tr/",
        "United Kingdom": "uk/",
        "Deutschland": "de/",
        "Italy": "it/",
        "France": "fr/",
        "Spain": "es/"
    }

    ASSERTIONS = {
        "Turkey": {"main_title": "Apple (Türkiye)",
                   "menu_text": "iPhone",
                   "iphone_title": "iPhone - Apple (TR)",
                   "menu_iphone_text": "iPhone 13 Pro\nYeni",
                   "pro_title": "iPhone 13 Pro ve iPhone 13 Pro Max - Apple (TR)",
                   "page_source": "Çantanız boş.",
                   "buy_button": "iPhone 13 Pro\nSatın Alın"},
        "United Kingdom": {"main_title": "Apple (United Kingdom)",
                           "menu_text": "iPhone",
                           "iphone_title": "iPhone - Apple (UK)",
                           "menu_iphone_text": "iPhone 13 Pro\nNew",
                           "pro_title": "iPhone 13 Pro and iPhone 13 Pro Max - Apple (UK)",
                           "page_source": "Your bag is empty.",
                           "buy_button": "Buy\niPhone 13 Pro"},
        "Deutschland": {"main_title": "Apple (Deutschland)",
                        "menu_text": "iPhone",
                        "iphone_title": "iPhone - Apple (DE)",
                        "menu_iphone_text": "iPhone 13 Pro\nNeu",
                        "pro_title": "iPhone 13 Pro und iPhone 13 Pro Max - Apple (DE)",
                        "page_source": "Deine Einkaufstasche ist leer.",
                        "buy_button": "Kaufen\niPhone 13 Pro"},
        "Italy": {"main_title": "Apple (Italia)",
                  "menu_text": "iPhone",
                  "iphone_title": "iPhone - Apple (IT)",
                  "menu_iphone_text": "iPhone 13 Pro\nNovità",
                  "pro_title": "iPhone 13 Pro e iPhone 13 Pro Max - Apple (IT)",
                  "page_source": "La shopping bag è vuota.",
                  "buy_button": "Acquista\niPhone 13 Pro"},
        "France": {"main_title": "Apple (France)",
                   "menu_text": "iPhone",
                   "iphone_title": "iPhone - Apple (FR)",
                   "menu_iphone_text": "iPhone 13 Pro\nNouveau",
                   "pro_title": "iPhone 13 Pro et iPhone 13 Pro Max - Apple (FR)",
                   "page_source": "Votre Panier est vide.",
                   "buy_button": "Acheter\niPhone 13 Pro"},
        "Spain": {"main_title": "Apple (España)",
                  "menu_text": "iPhone",
                  "iphone_title": "iPhone - Apple (ES)",
                  "menu_iphone_text": "iPhone 13 Pro\nNuevo",
                  "pro_title": "iPhone 13 Pro y iPhone 13 Pro Max - Apple (ES)",
                  "page_source": "Tu bolsa está vacía.",
                  "buy_button": "Comprar\niPhone 13 Pro"}

    }
