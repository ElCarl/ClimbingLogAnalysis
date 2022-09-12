from collections import defaultdict
import os
import climb_scoring
import data_import
import logbook

def summarise_stats(log: logbook.Logbook, scoring_method: climb_scoring.ScoringMethod):
    scores = defaultdict(list)
    failed_entries = 0
    for entry in log.ascents:
        try:
            entry_score = scoring_method.score_ascent(entry, log)
        except AttributeError:
            failed_entries += 1
        else:
            scores[entry.type].append(entry_score)
    
    print(f'{"Type":12}{"Count":8}{"Total":8}{"Mean":8}')
    print("-----------------------------------------")
    for k, v in scores.items():
        print(f"{k:12}{len(v):8}{sum(v):8.1f}{sum(v)/len(v):8.2f}")


def main():
    file_relative_location = "data"
    file_name = "Carl_Logbook.xlsx"
    full_path = os.path.join(file_relative_location, file_name)

    log = data_import.UKCImport.import_from_xlsx(full_path, "Carl")

    total_score = 0
    total_non_none_entries = 0
    total_none_entries = 0

    for entry in log.ascents:
        # print(f"{entry.date}: {entry.name} ({entry.grade}) - {entry.style}")
        try:
            entry_score = climb_scoring.FlatScoring.score_ascent(entry, None)
        except AttributeError:
            total_none_entries += 1
        else:
            total_non_none_entries += 1
            total_score += entry_score
    
    mean_score = total_score / total_non_none_entries
    
    print(f"{total_non_none_entries} climbs: {total_score} points. Mean score {mean_score:.2f}")

    summarise_stats(log, climb_scoring.FlatScoring)


if __name__ == "__main__":
    main()