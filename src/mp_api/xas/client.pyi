from typing import List, Optional
from mp_api.xas.models import XASDoc


class XASRester:

    def get_document_by_id(
            self,
            document_id: str,
            fields: Optional[List[str]] = None,
            monty_decode: bool = True,
            version: Optional[str] = None,
    ) -> XASDoc:
        ...
