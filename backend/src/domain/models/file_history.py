import json
from datetime import datetime

class FileHistory:
  def __init__(self, filename: str, size: int, amount_registers: int) -> None:
    self.filename = filename
    self.size = size
    self.amount_registers = amount_registers
    self.timestamp=datetime.now()

  @property
  def to_dict(self):
    return {
      "filename": self.filename,
      "size": self.size,
      "amount_registers": self.amount_registers,
      "timestamp": str(self.timestamp)
    }

  def __str__(self):
    json_class = {
        "filename": self.filename,
        "size": self.size,
        "amount_registers": self.amount_registers
    }
    return json.dumps(json_class)
