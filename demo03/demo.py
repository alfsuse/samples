import os
import json
from tensorflow.python.lib.io import file_io as file_io

static_html_path = os.path.join('/output/', 'demo.html')
rendered_template = """
    <html>
        <head>
            <title>correlation image</title>
        </head>
        <body>
            <img src={}>
        </body>
    </html>""".format(static_html_path)


file_io.write_string_to_file(static_html_path, rendered_template)



metadata = {
'outputs' : [{
    'type': 'web-app',
    'storage': 'inline',
    'source': '/output/demo.html',
}, {
    'type': 'web-app',
    'storage': 'inline',
}]
}
with file_io.FileIO('/mlpipeline-ui-metadata.json', 'w') as f:
    json.dump(metadata, f)
