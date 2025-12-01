import re
import codecs
def delete_html_tags(html_file, result_file):
        with codecs.open(html_file, 'r', 'utf-8') as file:
            html = file.read()
            clean_text = re.sub(r'<[^>]+>', '', html)
            with codecs.open(result_file, 'w', 'utf-8') as res_file:
                res_file.write(clean_text)
input_file = 'draft.html'
output_file = 'cleaned.txt'
delete_html_tags(input_file, output_file)
#видаляємо порожні рядки
with codecs.open(output_file, 'r', 'utf-8') as infile:
    lines = infile.readlines()
non_empty_lines = []
for line in lines:
    if line.strip():
        non_empty_lines.append(line)
with codecs.open(output_file, 'w', 'utf-8') as outfile:
    outfile.writelines(non_empty_lines)