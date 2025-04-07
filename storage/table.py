from typing import Any, List, Dict

class Table:
    """
    >> Class that represents a data table.
    """

    def __init__(self, data: None | List[List[Any]] | Dict[str, List[Any]] = None) -> None:
        """
        Initializes the Table.
      
        Args:
            data None | List[List[Any]] | Dict[str, List[Any]]: 
            The initial data. Can be:
                - None
                - A list of lists (matrix)
                - A dictionary with string keys and values as lists of any type.

        Raises:
            TypeError: If data is not of the types listed above.
        """
        if data is None:
            self._data: Dict[str, List[Any]] = {}
        # TODO: type(data) validation
        elif isinstance(data, dict):
            self._data: Dict[str, List[Any]] = data
        else:
            raise TypeError("data must be of type Dict[str, List[Any]], List[List[Any]] or None")
