def md5Checksum(path, file):
	filepath = path + '\\' + file
	fh = open(filepath, 'rb')
	md5 = hashlib.md5()
	while True:
		data = fh.read(1024)
		if not data:
			break
		md5.update(data)
	return md5.hexdigest()	