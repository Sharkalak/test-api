from fastapi import FastAPI
import uvicorn
from CoolProp.CoolProp import PhaseSI, PropsSI, get_global_param_string
r = PropsSI('T','P',P,'Q',Q,'Water')
print(f"{r}")
app = FastAPI()


@app.get("/demo/")
def demo(Q: int,P: int):
  
    return PropsSI('T','P',P,'Q',Q,'Water')
if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8080)
