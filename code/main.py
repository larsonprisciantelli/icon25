import pandas as pd
import recommender as rec
import classification as clf
import KB


#funzione per l'inserimento dei dati del film dall'utente
def getUserMovie(choice):
    title = input("Inserire il nome del film o serie TV che hai apprezzato: ").lower()
    typeM = input(title + ' è un film? (s/n) \n -> ').lower()
    while (str(typeM) != 's' and str(typeM) != 'n'):
        typeM = input("Inserisci un'opzione valida --> ")
    if typeM == 's':
        typeM = 'Movie'
    else:
        typeM = 'TV Show'
    country = input('Inserire il paese di produzione: \n -> ').lower()
    yr = input ('Inserire l`anno di rilascio: \n -> ').lower()
    yr=releaseYear(yr)
    cast = input('Inserire un membro del cast: \n -> ').lower()
    rating = input('Inserire un voto da 1 a 10 sul film/serie TV: \n -> ').lower()
    genreM=''
    if choice == 1:
        genreM = input('Inserisci il genere, scegliendo tra questi:\n1 action \n2 anime \n3 commedies \n4 cult \n5 documentary \n6 dramas \n7 fantasy \n8 horror \n9 kids \n10 musical \n11 nature \n12 romantic \n13 sport \n14 stand-up \n15 thrillers\n ->').lower()
        if (genreM == '1'):
            genreM = 'action'
        elif (genreM == '2'):
            genreM = 'anime'
        elif (genreM == '3'):
            genreM = 'comedies'
        elif (genreM == '4'):
            genreM = 'cult'
        elif (genreM == '5'):
            genreM = 'documentary'
        elif (genreM == '6'):
            genreM = 'dramas'
        elif (genreM == '7'):
            genreM = 'fantasy'
        elif (genreM == '8'):
            genreM = 'horror'
        elif (genreM == '9'):
            genreM = 'kids'
        elif (genreM == '10'):
            genreM = 'musical'
        elif (genreM == '11'):
            genreM = 'nature'
        elif (genreM == '12'):
            genreM = 'romantic'
        elif (genreM == '13'):
            genreM = 'sport'
        elif (genreM == '14'):
            genreM = 'standup'
        elif (genreM == '15'):
            genreM = 'thrillers' 
        else:
            while (not 1 <= int(genreM) <= 15):
                genreM = input("Perfavore, inserisci un numero corretto.\n") 
    data = {'type':[typeM],'title':[title],'cast':[cast],'genre': [genreM],'country':[country],'year_range':[yr],'ratings':[rating]}
    userMovieDF = pd.DataFrame(data)
    return userMovieDF


#funzione del menu principale
def menu():
    print("Benvenuto in UnibaVision!")
    choice = input("Scegli come proseguire: \n 1. Lasciati suggerire un nuovo film sulla base di un altro che hai apprezzato \n 2. Scopri il genere di un film o serie TV \n 3. Interroga il sistema \n 4. Esci\n --> ")
    while (int(choice) != 1 and int(choice) != 2 and int(choice) != 3 and int(choice) != 4):
        choice = input("Inserisci un'opzione valida --> ")
    return int(choice)


#funzione calcolo range anno di rilascio
def releaseYear(year):
    yearI=int(year)
    
    if (yearI < 1950):
            year = '<1950'
    elif (yearI >= 1950 and yearI < 1960):
            year ='1950-1960'
    elif (yearI >= 1960 and yearI < 1970):
            year ='1960-1970'
    elif (yearI >= 1970 and yearI < 1980):
            year ='1970-1980'
    elif (yearI >= 1980 and yearI < 1990):
            year ='1980-1990'
    elif (yearI >= 1990 and yearI < 1995):
            year ='1990-1995'
    elif (yearI >= 1995 and yearI < 2000):
            year ='1995-2000'
    elif (yearI >= 2000 and yearI < 2005):
            year ='2000-2005'
    elif (yearI >= 2005 and yearI < 2010):
            year ='2005-2010'
    elif (yearI >= 2010 and yearI < 2015):
            year ='2010-2015'
    elif (yearI >= 2015 and yearI <= 2020):
            year ='2015-2020'
    return year

def main():
    #preprocessing dei dati
    #prep.main()
    choice = 0
    while choice!=4:
        #menu
        choice = menu()
        
        if choice == 1:
            print('INIZIAMO! \n')
            userMovie = getUserMovie(choice)
            #recommender system
            rec.main(userMovie)
        if choice == 2:
            print('INIZIAMO! \n')
            userMovie = getUserMovie(choice)
            #predizione genere
            clf.main(userMovie)
        if choice == 3:
            print('INIZIAMO! \n')
            #interrogazione della base di conoscenza sul film
            KB.mainFunz()
        if choice == 4:
            print('Uscita...\n')
            break
 
if __name__ == "__main__":
    main()