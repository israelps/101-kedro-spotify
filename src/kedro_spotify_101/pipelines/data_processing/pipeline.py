from kedro.pipeline import Pipeline, node

from .nodes import preprocess_raw, merge_datasets


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=merge_datasets,
                inputs=["song_info", "song_metrics", "song_popularity"],
                outputs="int_spotify_data",
                name="merge_raw_data_node",
            ),
            node(
                func=preprocess_raw,
                inputs="int_spotify_data",
                outputs="prm_spotify_data",
                name="preprocess_data_node",
            ),
        ]
    )
