import re
def delete_html_tags(input_filepath, output_filepath):
    try:
        with open(input_filepath, 'r', encoding='utf-8') as infile:
            html_content = infile.read()
    except FileNotFoundError:
        print(f"Помилка: файл '{input_filepath}' не знайдено.")
        return
    except Exception as e:
        print(f"Помилка при читанні файлу '{input_filepath}': {e}")
        return
    clean_text = re.sub(r'<[^>]+>', '', html_content)
    try:
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(clean_text)
        print(f"Текст успішно очищено та збережено у файл '{output_filepath}'.")
    except Exception as e:
        print(f"Помилка при записі у файл '{output_filepath}': {e}")
input_file = 'draft.html'
output_file = 'cleaned.txt'
delete_html_tags(input_file, output_file)