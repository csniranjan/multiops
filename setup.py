from setuptools import setup, find_packages


setup(
    name="multiops",
    version="0.1.0",
    description="MultiOps - MLFlow for Training, Tracking and Multi Deployment",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    # Require MLflow as a dependency of the plugin, so that plugin users can simply install
    # the plugin & then immediately use it with MLflow
    install_requires=[
        "torchserve",
        "torch-model-archiver",
        "tritonclient[all]",
        "ray[serve]>=1.7.0",
        "mlflow>=1.15.0",
        # "-r requirements.txt",
    ],
    entry_points={
        "mlflow.deployments": [
            "ray-serve=rayserve",
            "torchserve=torchserve",
            "triton=triton.deployments",
        ],
    },
    # license="Apache 2.0",
)
