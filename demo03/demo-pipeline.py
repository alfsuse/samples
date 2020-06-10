
from kfp import compiler
import kfp.dsl as dsl

def gcs_download_op(url):
    return dsl.ContainerOp(
        name='Demo - Download',
        image='gcr.io/kaggle-images/python',
        command=['sh', '-c'],
        arguments=['wget $0 | tee /tmp/demo.py ', url, '/tmp/demo.py'],
        file_outputs={
            'data': '/tmp/demo.py',
        }
    )


def echo_op(text):
    return dsl.ContainerOp(
        name='echo',
        image='gcr.io/kaggle-images/python',
        command=['sh', '-c'],
        arguments=['python3 -c "$0"', text],
        output_artifact_paths={'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'})

@dsl.pipeline(
    name='Sequential pipeline',
    description='A pipeline with two sequential steps.'
)
def sequential_pipeline(url='https://raw.githubusercontent.com/alfsuse/samples/master/demo03/demo.py'):
    """A pipeline with two sequential steps."""

    download_task = gcs_download_op(url)
    echo_task = echo_op(download_task.output)

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(sequential_pipeline, __file__ + '.tar.gz')