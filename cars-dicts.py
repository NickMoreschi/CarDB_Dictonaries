import DBManager
import CLI
import FileManager

def main():
    dbm = DBManager.DBManager()
    fm = FileManager.FileManager(dbm)
    
    cli = CLI.CLI(dbm, fm)
    cli.run_cli()
    
    
main()