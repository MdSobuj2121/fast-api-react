from sqlalchemy import create_engine, MetaData
engine = create_engine('mysql+pymysql://root@localhost:3306/fast_api_crud')
con = engine.connect()
meta = MetaData()
