import hashlib

def md5Checksum(path, file):
	"""
		Gets the md5 checksum from the specified file
	"""
	filepath = path + '\\' + file
	fh = open(filepath, 'rb')
	md5 = hashlib.md5()
	while True:
		data = fh.read(1024)
		if not data:
			break
		md5.update(data)
	return md5.hexdigest()	