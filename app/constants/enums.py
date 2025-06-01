import enum

class InputTypeEnum(str, enum.Enum):
    video = "video"
    document = "document"
    audio = "audio"

class StatusEnum(str, enum.Enum):
    pending = "pending"
    processing = "processing"
    completed = "completed"
    failed = "failed"

 