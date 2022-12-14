import os
from datetime import datetime
import pandas
from climb_grading import Grade, Style
from climb_scoring import FlatScoring
import logbook

class UKCImport:
    main_style_strings = {
        "": Style.MainStyle.NONE,
        "-": Style.MainStyle.NONE,
        "Lead": Style.MainStyle.LEAD,
        "Solo": Style.MainStyle.SOLO,
        "Sent": Style.MainStyle.BOULDER,
        "2nd": Style.MainStyle.SECOND,
        "AltLd": Style.MainStyle.ALT_LEAD,
        "TR": Style.MainStyle.TOP_ROPE,
        "DWS": Style.MainStyle.DWS
    }

    sub_style_strings = {
        "": Style.SubStyle.NONE,
        "O/S": Style.SubStyle.ONSIGHT,
        "&beta": Style.SubStyle.FLASH,
        "&beta;": Style.SubStyle.FLASH,
        "β": Style.SubStyle.FLASH,
        "G/U": Style.SubStyle.GROUND_UP,
        "RP": Style.SubStyle.REDPOINT,
        "x": Style.SubStyle.REDPOINT,
        "rpt": Style.SubStyle.REPEAT,
        "dog": Style.SubStyle.DOG,
        "dnf": Style.SubStyle.DNF
    }

    # Could also have a method to import via web scraping?
    def import_from_xlsx(file_path, climber_name):
        log = logbook.Logbook(climber_name)
        data_frame = pandas.read_excel(file_path)
        data_frame.reset_index()

        for _, row in data_frame.iterrows():
            ascent = UKCImport._interpret_logbook_entry(row)
            log.add_ascent(ascent)
        
        return log

    def _interpret_logbook_entry(row_data):
        climb_name = row_data["Climb name"]
        grade_text = row_data["Grade"]
        style_text = row_data["Style"]
        date_text = row_data["Date"]

        grade, climb_type, stars = UKCImport._extract_grade_and_quality(grade_text)

        style = UKCImport._extract_style(style_text)

        ascent_date = datetime.strptime(date_text, "%d/%b/%y").date()

        return logbook.Ascent(climb_name, ascent_date, grade, climb_type, style, stars)
    
    def _extract_grade_and_quality(grade_text):
        split_grade_text = grade_text.split(" ")

        if split_grade_text == []:
            return None, None, None

        # First bit will always be the main grade
        if split_grade_text[0] != "":
            try:
                grade = Grade(split_grade_text[0])
                climb_type = grade.climb_type
            except TypeError:
                grade, climb_type = None, None
        else:
            raise ValueError

        # Last bit will be the number of stars
        if split_grade_text[-1] == "":
            stars = 0
        elif split_grade_text[-1][0] == "*":
            stars = len(split_grade_text[-1])
        else:
            stars = 0

        return grade, climb_type, stars

    @classmethod
    def _extract_style(cls, style_text):
        # Default to none
        main_style = Style.MainStyle.NONE
        sub_style = Style.SubStyle.NONE

        split_text = style_text.split()

        if len(split_text) == 2:
            main_text, sub_text = split_text
            main_style = cls.main_style_strings[main_text]
            sub_style = cls.sub_style_strings[sub_text]
        elif len(split_text) == 1:
            main_text = split_text[0]
            main_style = cls.main_style_strings[main_text]
            sub_style = Style.SubStyle.NONE
        else:
            pass # Leave styles as none

        return Style(main_style, sub_style)

