from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ReportCardItem(BaseModel):
    targetId: str
    inputList: list[str]

# 이미 생성된 리포트 카드의 ID를 저장할 Set
created_report_cards = set()

@app.post("/create_report_card")
async def create_report_card(item: ReportCardItem):
    target_id = item.targetId

    # 이미 생성된 리포트 카드인지 확인
    if target_id not in created_report_cards:
        # 여기에서 데이터베이스에 저장하거나 다른 작업 수행 가능
        created_report_cards.add(target_id)
        
        return {"message": f"Report card with id {target_id} created successfully."}
    else:
        raise HTTPException(status_code=400, detail=f"Report card with id {target_id} already exists.")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
