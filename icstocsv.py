from csv_ical import Convert

convert = Convert()
convert.ICS_FILE_LOCATION = 'ADECal.ics'
convert.CSV_FILE_LOCATION = 'ADECal.csv'

convert.read_ical(convert.ICS_FILE_LOCATION)

convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)