from fastapi import FastAPI
from app.api.v1.endpoints import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Main Page"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: None):
    return {"item_id": item_id, "q": q}


def main():
    print("Hello from fastapi!")


if __name__ == "__main__":
    main()
