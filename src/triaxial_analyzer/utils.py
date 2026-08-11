"""
General helper functions.
"""


def normalize_columns(df):
    """
    Normalize DataFrame column names (lowercase, strip spaces).

    Parameters:
        df: pandas DataFrame.

    Returns:
        Modified DataFrame.
    """
    df.columns = [c.strip().lower() for c in df.columns]
    return df
