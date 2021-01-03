from PyPDF2 import PdfFileWriter, PdfFileReader
import os
print("""
Inserisci il File da criptare nella stessa cartella di questo programma!!!""")

def secure_pdf(file,password):
    if not os.path.isfile(file): #se non è un file esco
        print("Il file inserito non esiste o non è un file!")
        return None
    if file.endswith(".pdf") or file.endswith(".PDF"): #se è un file pdf procedo
        if not os.path.isdir(r".\File Criptati"): #Creo la cartella File Criptati se non esiste
            os.mkdir(r".\File Criptati")
        file_protetto = PdfFileWriter()
        file_da_proteggere = PdfFileReader(file)
        print("Sto creando il file criptato...")
        for page in range(file_da_proteggere.numPages):
            file_protetto.addPage(file_da_proteggere.getPage(page))
        file_protetto.encrypt(password)
        with open(f".\\File Criptati\\encrypted_{file}","wb") as f:
            file_protetto.write(f)
            f.close()
        print(f"Creata versione criptata di {file}")
    else:                               #se non è un file pdf esco
        print("Il file inserito non è un PDF!")
        return None


file=input("Inserisci il nome del file PDF da criptare: ")
password=input("Inserisci la password che vuoi assegnare al file: ")
secure_pdf(file,password)
input("")

