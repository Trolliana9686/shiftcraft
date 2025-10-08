from fastapi import FastAPI
app=FastAPI(title='ShiftCraft')
@app.get('/')
def r(): return {'ok':True,'service':'shiftcraft'}
