import pandas as pd


def bookmark():
    format_txt = """
#BookMark
    """
    res = {}
    df = pd.read_csv("bookmark.csv")
    for _, item in df.iterrows():
        tag = item["tag"]
        if tag not in res:
            res[tag] = []
        res[tag].append(
            f"* [{item['name']}]({item['site_url']})  {item['info'] if item['info'] else ''}"
        )
    res = sorted(res.items(), key=lambda d: d[0])
    for k, s in res:
        format_txt += "\n" + k
        for i in s:
            format_txt += "\n" + i
    with open("bookmark.md", "w+") as f:
        f.write(format_txt)


bookmark()
