@ECHO OFF

IF EXIST backup.sql DEL backup.sql

SET PGPASSWORD=2004
SET USER=ioana
SET DB=dj2025
SET HOST=localhost
SET PORT=5432

ECHO Pornim backup...

FOR %%t IN (
    "magazin_haine_brand"
    "magazin_haine_categorie"
    "magazin_haine_colectie"
    "magazin_haine_colectie_produs"
    "magazin_haine_contact"
    "magazin_haine_material"
    "magazin_haine_produs"
    "magazin_haine_produs_materiale"
    "magazin_haine_variantaprodus"
) DO (
    ECHO Exportam tabelul %%t...
    pg_dump --column-inserts --data-only --inserts --schema=django -h %HOST% -U %USER% -p %PORT% -d %DB% -t django.%%t >> backup.sql
)

SET PGPASSWORD=

ECHO Backup finalizat cu succes!
PAUSE
