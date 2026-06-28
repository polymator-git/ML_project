def statistics_to_dict(statistics):
    stats = {}

    for item in statistics:
        stats[item["type"]] = item["value"]

    return stats