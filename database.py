from sqlalchemy import create_engine, text

engine = create_engine('postgresql+psycopg2://postgres:XVGT4EKwTfC9L6Vw@db.dtxpydmjiucxcwzrjoau.supabase.co/postgres')


def load_drives():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM drives"))
    drives = []
    for row in result:
      drives.append(dict(row._mapping))
    return drives