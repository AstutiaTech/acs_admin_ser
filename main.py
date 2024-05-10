from fastapi import FastAPI, Request, status, Depends, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import sys, traceback

#routers
from routes import seed
from routes.v1.authentication import auth
from routes.v1.base import owner
from routes.v1.base import user

app = FastAPI()

app.include_router(seed.router)
app.include_router(auth.router)
app.include_router(owner.router)
app.include_router(user.router)

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
        response.headers["Expires"] = "0"
        response.headers["Pragma"] = "no-cache"
        return response
    except Exception as e:
        err = "Stack Trace - %s \n" % (traceback.format_exc())
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=jsonable_encoder({"detail": str(err)}))


app.middleware('http')(catch_exceptions_middleware)

@app.get("/")
async def root():
    return {"message": "hello World!!"}
