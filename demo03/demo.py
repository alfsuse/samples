import os
import json
from tensorflow.python.lib.io import file_io as file_io
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory

static_html_path = os.path.join('/output/', 'demo.html')
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
