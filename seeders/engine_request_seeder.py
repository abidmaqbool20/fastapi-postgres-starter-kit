from sqlalchemy.orm import Session
from app.models.engine_request import EngineRequest, InputTypeEnum, StatusEnum
from app.config.database import Base 

def seed_engine_requests(db: Session):   
    dummy_requests = [
        EngineRequest(
            user_id=1,
            input_type=InputTypeEnum.video,
            input_url="/videos/sample1.mp4",
            result_json={"summary": "test result"},
            status=StatusEnum.completed,
        ),
        EngineRequest(
            user_id=2,
            input_type=InputTypeEnum.document,
            input_url="/documents/report.pdf",
            result_json=None,
            status=StatusEnum.pending,
        ),
        EngineRequest(
            user_id=2,
            input_type=InputTypeEnum.audio,
            input_url="/audios/audio.mp3",
            result_json=None,
            status=StatusEnum.pending,
        )
    ]

    for req in dummy_requests:
        exists = db.query(EngineRequest).filter_by(input_url=req.input_url).first()
        if not exists:
            print(f"Adding new engine request: {req.input_url}")
            db.add(req)
        else:
            print(f"Already exists: {req.input_url}")

    db.commit()
    print("Seeding complete.")
