"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from kedro_spotify_101.pipelines import data_processing


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    return {
        "__default__": data_processing.create_pipeline(),
        "data_processing_pipeline": data_processing.create_pipeline(),
    }
