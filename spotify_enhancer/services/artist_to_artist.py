from typing import Any

from spotify_enhancer.algorithms import generate_items_flowchart


def get_artist_to_artist_flowchart(
    source_spotify_artist_id: str,
    target_spotify_artist_id: str,
    get_neighbors: Any
) -> list[str]:
    artists_uri_flowchart = generate_items_flowchart(
        source_spotify_artist_id,
        target_spotify_artist_id,
        get_neighbors
    )

    return artists_uri_flowchart
