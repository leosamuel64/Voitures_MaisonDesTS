import sqlite3


def get_trajets():
    """
    Ajoute un utilisateur dans la base de données SQL
    """
    connection = sqlite3.connect('gsea-cours')

    request = """
    SELECT Trajets.id, Voitures.nom, Trajets.date
    FROM Trajets
    JOIN Voitures ON Trajets.id_voiture=Voitures.id
    """

    cursor = connection.execute(request)
    res=[]
    for x in cursor:
        if x!=None:
            res.append(x)
    
    connection.commit()
    connection.close()
    return res

def compte(id,mois):
    connection = sqlite3.connect('gsea-cours')
    request = """
    SELECT COUNT(id)
    FROM Trajets
    WHERE id_voiture="""+str(id)+" and date LIKE '"+str(mois)+"%'"
    
    print(request)
    cursor = connection.execute(request)
    res=[]
    for x in cursor:
        if x!=None:
            res.append(x)
    return res[0][0]
    

def SuppTrajets(id):
    """
    Change le mot de passe dans la base de données SQL
    """
    connection = sqlite3.connect('gsea-cours')

    request = """
    DELETE from Trajets
        where id='"""+id+"'"

    connection.execute(request)
    connection.commit()
    connection.close()

def add_membreData(idVoiture, date):
    """
    Change le mot de passe dans la base de données SQL
    """
    connection = sqlite3.connect('gsea-cours')

    request = "INSERT INTO Trajets (id_voiture, date) VALUES ('"+str(idVoiture)+"','"+str(date)+"');"

    connection.execute(request)
    connection.commit()
    connection.close()

