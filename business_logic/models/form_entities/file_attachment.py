import uuid;
from dataclasses import field

class FileAttachment:
    file_guid: uuid.UUID = field(default_factory=uuid.uuid4)
    file_name:str = ""
    file_ending: str = ""
    mime_type: str = ""
    magic_byte_header: bytes = b""
    file_content: bytes = b""
