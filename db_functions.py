#importuju knihovnu pro práci s PostgreSQL
import psycopg2
import psycopg2.extras
#knihovna na interakci s operačním systémem
import os

#funkce pro spojení s databází
def get_db():
    url = os.getenv('DATABASE_URL')
    conn = psycopg2.connect(url, sslmode='require', cursor_factory=psycopg2.extras.NamedTupleCursor)
    return conn


def get_activities():
    #spojení s databází, linka mezi flaskem a mým počítačem
    db = get_db()
    #cursor = spouští sql dotazy, cursor() je součástí knihovny psychopg2, cursor mají všechny py knihovny s různými
    #databázemi PostgreSQL není databáze ale db ms = database management system
    cur = db.cursor()
    cur.exec('SELECT id_activity, type, duration, environment FROM activities')
    #cursor vrátí všechny záznamy dle sql dotazu a mám je u sebe a je třeba si o ně říci
    #fetchall() vrátí seznam všech řádků, fetchone() vrátí jeden řádek výsledků
    activities = cur.fetchall()
    #už po tobě nebudu chtít nic s tímto dotazem a s těmito výsledky
    cur.close()
    return activities




