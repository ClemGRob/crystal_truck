def write_from_sratch(content, doc_name="map.txt"):
    with open(doc_name, "w") as file:
        file.writelines(content)


def write_new_line(content, doc_name="map.txt"):
    with open(doc_name, "a") as file:
        # content = "%s" % out, "\n"
        file.writelines(content)


