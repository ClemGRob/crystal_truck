def write_from_sratch(content, doc_name = "map_bis.txt"):
	with open(doc_name, "w") as file:
		# content = "%s" % out, "\n"
		file.writelines(content)
		file.close()



def write_new_line(content,doc_name = "map_bis.txt"):
	with open(doc_name, "a") as file:
		# content = "%s" % out, "\n"
		file.writelines(content)
		file.close()

		
def print_doc(doc_name = "map_bis.txt"):
	with open(doc_name, "r") as file:
		content = file.read()
		print(content)
		file.close()
	