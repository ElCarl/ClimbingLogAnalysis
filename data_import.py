import os
import pandas
import logbook

class LogbookImport:
    def __init__(self, climber_name):
        self.climber_name = climber_name
        self.ascents = []
    def import_from_ukc_xlsx(self, file_path):
        pass

        

def main():
    file_path = "data"
    file_name = "Carl_Logbook.xlsx"
    full_path = os.path.join(file_path, file_name)

if __name__ == "__main__":
    main()