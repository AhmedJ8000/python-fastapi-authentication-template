from fastapi import FastAPI, Depends
from controllers.teas import router as TeasRouter
from controllers.comments import router as CommentsRouter
from controllers.users import router as UserRouter

app = FastAPI()

app.include_router(TeasRouter, prefix="/api")
app.include_router(CommentsRouter, prefix="/api")
app.include_router(UserRouter, prefix="/api")


# Example middleware
def help():
    return "SOS noooooow!!!!!"

@app.get("/")
def home(mamamia: str = Depends(help)):
    return {"message": mamamia}
