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