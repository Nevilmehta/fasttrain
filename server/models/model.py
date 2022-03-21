from msilib.schema import Class
from typing import List
from pydantic import BaseModel

class request(BaseModel):

    oper:List[str]