import asyncio
import json
import os

from googletrans import Translator

input_file = "src/plugins/i18n/locales/ru.json"

with open(input_file, "r", encoding="utf-8") as f:
    source_data = json.load(f)

output_files = [
    ("src/plugins/i18n/locales/uz.json", "uz"),
    ("src/plugins/i18n/locales/tj.json", "tg"),
    ("src/plugins/i18n/locales/en.json", "en"),
]

for output_file in output_files:
    translated_data = {}
    if os.path.exists(output_file[0]):
        with open(output_file[0], "r", encoding="utf-8") as f:
            translated_data = json.load(f)

    translator = Translator()


    async def translate_value(value, existing=None):
        if isinstance(value, str):
            if value.strip():
                if existing:  # Return existing translation if present
                    return existing
                try:
                    result = await translator.translate(value, src='ru', dest=output_file[1])
                    return result.text
                except Exception as e:
                    print(f"Translation error: {e}")
                    return value
            else:
                return value
        elif isinstance(value, dict):
            return {
                k: await translate_value(v, existing.get(k) if isinstance(existing, dict) else None)
                for k, v in value.items()
            }
        elif isinstance(value, list):
            return [
                await translate_value(v, existing[i] if isinstance(existing, list) and i < len(existing) else None)
                for i, v in enumerate(value)
            ]
        return value


    merged_data = asyncio.run(translate_value(source_data, translated_data))

    with open(output_file[0], "w", encoding="utf-8") as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Translation complete! File saved ad {output_file[0]}")
