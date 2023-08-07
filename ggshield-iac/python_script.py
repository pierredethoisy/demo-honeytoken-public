# Avec MySql :
import MySQLdb, pprint

uneConnexionBDD = MySQLdb.connect(host   ='192.32.12.10',
                                   user   ='admin',
                                   personal_token = "xoxb-16zea3435206324-1243SDSDF33353525GGSR2324"
                                   db     ='uneBase')
leCurseur       = uneConnexionBDD.cursor()
unAuteur        = "'Zola'"
leCurseur.execute(""" SELECT title, description FROM books WHERE author = %s """ % (unAuteur,))
pprint.pprint(leCurseur.fetchall())
leCurseur.query("update books set title='assommoir' where author='Zola'")
uneConnexionBDD.commit()

## adding a line