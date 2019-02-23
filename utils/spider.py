from constants.spider import FILE_SUFFIX_LANG_MAPPING, LangType, SUFFIX_IGNORE


def get_lang_by_stats(stats: dict) -> LangType:
    """
    :param stats: stats is generated by utils.file.get_file_suffix_stats
    :return:
    """
    data = stats.items()
    data = sorted(data, key=lambda item: item[1])
    data = list(filter(lambda item: item[0] not in SUFFIX_IGNORE, data))
    top_suffix = data[-1][0]
    if FILE_SUFFIX_LANG_MAPPING.get(top_suffix) is not None:
        return FILE_SUFFIX_LANG_MAPPING.get(top_suffix)
    return LangType.OTHER